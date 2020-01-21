import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(dotenv_path='./.env')


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = ('true' == os.environ.get("DB_TRACK_MODIFICATIONS"))