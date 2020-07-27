import os


class DebugConfig:
    ENV = 'development'
    DEBUG = True
    SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.environ["UPLOAD_FOLDER"]
    MAX_CONTENT_LENGTH= 50 * 1024 * 1024
