from os import getenv, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv()


class Config:
    SECRET_KEY = getenv('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

