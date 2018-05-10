# -*- coding: UTF-8 -*-
from flask import Flask, redirect, url_for
from app.flask_adminlte import AdminLTE

from app.blueprints import all_blueprints
from importlib import import_module

from app.views.auth import login_manager


def create_app():
    flask_app = Flask(__name__, instance_relative_config=True)
    AdminLTE(flask_app)

    flask_app.secret_key = 'LearnFlaskTheHardWay2017'
    login_manager.init_app(flask_app)

    for bp in all_blueprints:
        import_module(bp.import_name)
        flask_app.register_blueprint(bp)

    return flask_app


if __name__ == "__main__":
    flask_app = create_app()
    flask_app.run(host='0.0.0.0', port=5000, debug=True)
