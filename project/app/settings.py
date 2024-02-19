from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

ENV = 'developmnet'
SECRET_KEY = 'dev'

SQLALCHEMY_COMMIT_ON_TEARDOWN = True

SQLALCHEMY_TRACK_MODIFICATIONS = True

PORT = 5007
HOST = '0.0.0.0'
