import os

MONGO_URI = os.environ.get('MONGO_URI')

JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')

JWT_TOKEN_LOCATION = os.environ.get('JWT_TOKEN_LOCATION')

JWT_COOKIE_CSRF_PROTECT = os.environ.get('JWT_COOKIE_CSRF_PROTECT')
