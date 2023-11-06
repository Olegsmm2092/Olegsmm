import os, binascii
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

JSONIFY_PRETTYPRINT_REGULAR = os.environ.get('JSONIFY_PRETTYPRINT_REGULAR', False)
JSON_SORT_KEYS = os.environ.get('JSON_SORT_KEYS', True)
JSONIFY_MIMETYPE = os.environ.get('JSONIFY_MIMETYPE', "application/json")
FLASK_RUN_HOST = os.environ.get("FLASK_RUN_HOST", "0.0.0.0")
FLASK_RUN_PORT = os.environ.get("FLASK_RUN_PORT", 8001)
FLASK_DEBUG = os.environ.get("FLASK_DEBUG", 0)
SQLALCHEMY_ECHO = os.environ.get("SQLALCHEMY_ECHO", 0)
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS", 0)
SECRET_KEY = os.environ.get('SECRET_KEY', binascii.hexlify(os.urandom(24)))
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
