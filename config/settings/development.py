from .base import *

DEBUG = True
ALLOWED_HOSTS = [
    "localhost", 
    "127.0.0.1"
    ]
STATICFILES_DIRS = [
    BASE_DIR / ".." / "core" / "static",
    ]