import os
import requests

DEBUG = False
APP_MODE = "DEVELOPMENT"
ALLOWED_HOSTS = []
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = []
CSRF_TRUSTED_ORIGINS = []

if os.environ.get("ECS_CONTAINER_METADATA_URI_V4"):
    try:
        container_metadata = requests.get(
            os.environ["ECS_CONTAINER_METADATA_URI_V4"]
        ).json()
        ALLOWED_HOSTS.append(container_metadata["Networks"][0]["IPv4Addresses"][0])
    except:
        pass
