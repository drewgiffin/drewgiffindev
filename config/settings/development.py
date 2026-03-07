from .base import *
load_dotenv(f"{BASE_DIR}/.env.development")

DEBUG = True
ALLOWED_HOSTS = [
    "localhost", 
    "127.0.0.1"
    ]

SECRET_KEY = os.getenv("SECRET_KEY")
