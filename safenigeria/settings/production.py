from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SAFE_NIGERIA_SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = []
