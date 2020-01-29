import os
# from os.path import join, dirname
# from dotenv import load_dotenv
# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)

MONGO_URI = os.environ.get('MONGO_URI')

JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')

JWT_BLACKLIST_ENABLED = os.environ.get('JWT_BLACKLIST_ENABLED')

JWT_TOKEN_LOCATION = os.environ.get('JWT_TOKEN_LOCATION')