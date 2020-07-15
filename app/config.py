import os

class DebugConfig:
    ENV = 'development'
    DEBUG = True
    SECRET_KEY = 'so_secret'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost:5432/file_storage'
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/')
    MAX_CONTENT_PATH = 50 * 1024 * 1024
