from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()


class File(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    expiration_time = db.Column(db.DateTime, nullable=False)


    @classmethod
    def add_file(cls, filename, expiration_time):
        file = cls(filename=filename, expiration_time=expiration_time)
        db.session.add(file)
        db.session.commit()
        return file.id

    @classmethod
    def get_file(cls, id):
        return cls.query.filter_by(id=id).first()
        