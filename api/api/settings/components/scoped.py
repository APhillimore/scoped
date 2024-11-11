import environ

env = environ.Env()

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "user.authentication.CognitoRemoteUserBackend",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("user.permissions.DenyAny",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_THROTTLE_RATES": {
        "anon": "1/day",
        "user": "30/minute",
    },
    "COERCE_DECIMAL_TO_STRING": False,
    "PAGE_SIZE": 100,
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Scoped API",
    "DESCRIPTION": "API for Scoped",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SERVE_PERMISSIONS": ["rest_framework.permissions.IsAdminUser"],
    "SCHEMA_PATH_PREFIX": r"/v[0-9]",
}


AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "user.authentication.CognitoRemoteUserBackend",
)

AUTH_USER_MODEL = "user.User"

SCOPED = {
    "AWS": {
        "REGION": env("AWS_REGION"),
        "COGNITO": {
            "USER_POOL_ID": env("COGNITO_USER_POOL_ID"),
            "CLIENT_IDS": env("COGNITO_CLIENT_IDS").split(","),
            "ENDPOINT": env("COGNITO_ENDPOINT"),
        },
    }
}
