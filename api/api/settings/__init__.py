# https://sobolevn.me/2017/04/managing-djangos-settings
# https://github.com/wemake-services/wemake-django-template
from pathlib import Path
import environ
import sys
import os
from split_settings.tools import include, optional

BASE_DIR = Path(__file__).resolve().parent.parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
env = environ.Env(DEBUG=(bool, False))

env = environ.Env(
    DEBUG=(bool, False),
    DATABASE_URL_RW=(str, ""),
    DATABASE_URL_RO=(str, ""),
    APP_MODE=(str, "PRODUCTION"),
)

base_settings = [
    "components/base.py",
    "components/caches.py",
    "components/database.py",
    "components/scoped.py",
    f"environments/{env('APP_MODE').lower()}.py",
    optional("environments/local.py"),
]

if "test" in sys.argv:  # pragma: no cover
    base_settings.append("environments/testing.py")

include(*base_settings)
