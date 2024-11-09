from drf_spectacular.extensions import OpenApiAuthenticationExtension


class CognitoRemoteUserBackendExtension(OpenApiAuthenticationExtension):
    target_class = "user.authentication.CognitoRemoteUserBackend"
    name = "CognitoRemoteUserBackend"

    def get_security_definition(self, auto_schema):
        return {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
        }
