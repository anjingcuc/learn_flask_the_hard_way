# -*- coding: UTF-8 -*-
from flask import Flask, redirect, url_for

from app.flask_adminlte import AdminLTE

from app.blueprints import all_blueprints
from importlib import import_module

from app.extentions import login_manager
from app.extentions import db
from app.extentions import bcrypt
from app.extentions import migrate

from config import config
import os


def create_app():
    flask_app = Flask(__name__, instance_relative_config=True)
    AdminLTE(flask_app)

    config_name = os.getenv('FLASK_CONFIG', 'default')
    flask_app.config.from_object(config[config_name])
    flask_app.config.from_pyfile('app.cfg', silent=True)

    login_manager.session_protection = 'AdminPassword4Me'
    login_manager.login_view = 'signin'
    login_manager.login_message = 'Unauthorized User.'
    login_manager.login_message_category = "info"
    
    login_manager.init_app(flask_app)
    db.init_app(flask_app)
    bcrypt.init_app(flask_app)
    migrate.init_app(flask_app, db)

    for bp in all_blueprints:
        import_module(bp.import_name)
        flask_app.register_blueprint(bp)

    return flask_app


if __name__ == "__main__":
    flask_app = create_app()
    flask_app.run(host='0.0.0.0', port=5000, debug=True)
