import environ

env = environ.Env()

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": env.db_url("DATABASE_URL_RW"),
}

DATABASES.update({"ro": env.db_url("DATABASE_URL_RO")})
DATABASES["ro"]["TEST"] = {"MIRROR": "default"}
