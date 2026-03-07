from .base import *
load_dotenv(f"{BASE_DIR}/.env.production")

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
EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
