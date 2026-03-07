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
