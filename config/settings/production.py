import os
from .base import *
from dotenv import load_dotenv

load_dotenv(str(BASE_DIR / ".." / ".env.development"))

DEBUG = False
ALLOWED_HOSTS = [
    "drewgiffin.dev",
    "www.drewgiffin.dev",
    "66.225.231.154",
]
STATIC_ROOT = "/var/www/drewgiffindev/static"

SECRET_KEY = os.getenv("SECRET_KEY")
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
