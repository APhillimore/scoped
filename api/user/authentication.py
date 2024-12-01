import jwt
import json
import requests
from django.http import HttpRequest
from django.core.cache import cache
from django.conf import settings
from django.contrib.auth.backends import RemoteUserBackend
from jwt.exceptions import PyJWTError


class JwkClient(jwt.PyJWKClient):
    """
    Custom JWK client with cache to reduce the number of requests to the Cognito server.
    """

    key_cache = "cognito_jwk_cache"

    def __init__(self, uri: str):
        super().__init__(uri)

    def fetch_data(self):
        if data := cache.get(self.key_cache):
            return data
        return cache.set(self.key_cache, super().fetch_data(), timeout=3600)


def get_user_claims(self, request):
    token = request.META.get("HTTP_AUTHORIZATION")[6:].strip(
        " "
    )  # remove 'Bearer ' from token
    try:
        client = JwkClient(
            f"https://cognito-idp.{settings.SPHERES['AWS']['REGION']}.amazonaws.com/{settings.SPHERES['AWS']['COGNITO']['USER_POOL_ID']}/.well-known/jwks.json"
        )
        signing_key = client.get_signing_key_from_jwt(token)
        claims = jwt.decode(
            token,
            signing_key.key,
            algorithms=["RS256"],
            issuer=f"https://cognito-idp.{settings.SPHERES['AWS']['REGION']}.amazonaws.com/{settings.SPHERES['AWS']['COGNITO']['USER_POOL_ID']}",
            options={
                "verif_signature": True,
                "verify_exp": True,
                "verify_nbf": True,
                "verify_iat": True,
                "verify_aud": False,
                "verify_iss": True,
            },
        )
        if claims["client_id"] not in settings.SPHERES["AWS"]["COGNITO"]["CLIENT_IDS"]:
            return False
    except PyJWTError as e:
        return False


class CognitoRemoteUserBackend(RemoteUserBackend):
    def get_user_claims(self, request):
        return get_user_claims(request)

    def configure_user(self, request, user):
        info = {}
        if claims := self.get_user_claims(request):
            if info := json.loads(self.get_user_info(request)):
                if info.get("given_name"):
                    user.first_name = info["given_name"]
                if info.get("family_name"):
                    user.last_name = info["family_name"]
                user.email = info.email
            user.remote_id = claims.sub
            user.set_unusable_password()
            user.save()
        return user

    def get_user_info(self, request: HttpRequest):
        token = request.META.get("HTTP_AUTHORIZATION")[6:].strip(" ")
        response = requests.get(
            f"https://{settings.SPHERES['AWS']['COGNITO']['ENDPOINT']}/oauth2/userInfo",
            headers={"Authorization": f"Bearer {token}"},
        )
        if response.ok:
            return response.text
        return False
