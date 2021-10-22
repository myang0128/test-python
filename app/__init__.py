from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
import os

from config import config_options

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    environment_configuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(config_options[environment_configuration])
    db.init_app(app)
    jwt = JWTManager(app)

    with app.app_context():
        from .models import Order, User
        db.create_all()
        from .order import order_api_blueprint
        app.register_blueprint(order_api_blueprint)

        from .auth import  auth_api_blueprint
        app.register_blueprint(auth_api_blueprint)
        return app
