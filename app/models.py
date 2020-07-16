from flask_sqlalchemy import SQLAlchemy
from flask import current_app
from datetime import datetime
import random
import string
db = SQLAlchemy()


class File(db.Model):
    file_id = db.Column(db.Integer, primary_key=True)
    file_url = db.Column(db.String(100), unique=True, nullable=False)
    file_path = db.Column(db.String(100), unique=True, nullable=False)
    expiration_time = db.Column(db.DateTime, nullable=False)

    @classmethod
    def __init__(cls, file_path, datetime):
        url = "127.0.0.1:5000/files/" + ''.join(string.ascii_lowercase + string.digits, k=8)
        file = cls(file_url=url, file_path=file_path, expiration_time=datetime)
        cls.save(file)

        