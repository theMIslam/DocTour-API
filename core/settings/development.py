from datetime import timedelta
from pathlib import Path
from core.settings.env_reader import env, csv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = ['*']
DEBUG = env("DEBUG", default=True, cast=bool)


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=7),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,
    "AUTH_HEADER_TYPES": ("Bearer", "JWT"),
}
