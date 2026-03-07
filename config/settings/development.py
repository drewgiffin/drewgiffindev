from .base import *
load_dotenv(f"{BASE_DIR}/.env.development")

DEBUG = True
ALLOWED_HOSTS = [
    "localhost", 
    "127.0.0.1"
    ]

SECRET_KEY = os.getenv("SECRET_KEY")
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
