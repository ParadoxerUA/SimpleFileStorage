from flask import Flask
from views import bp
from models import db


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    app.register_blueprint(bp)
    app.app_context().push()
    db.create_all()
    return app


if __name__ == '__main__':
    from config import DebugConfig
    app = create_app(DebugConfig)
    app.run()
