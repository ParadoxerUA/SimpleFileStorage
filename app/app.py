from flask import Flask
from werkzeug.utils import secure_filename
from .views import bp
from .models import db


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(DebugConfig)
    db.init_app(app)
    app.register_blueprint(bp)
    return app


if __name__ == '__main__':
    from config import DebugConfig
    app = create_app(DebugConfig)
    app.run()
