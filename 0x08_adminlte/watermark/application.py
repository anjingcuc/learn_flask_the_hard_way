from flask import Flask, redirect, url_for
from watermark.flask_adminlte import AdminLTE

from watermark.blueprints import all_blueprints
from importlib import import_module

from watermark.views.auth import login_manager


def create_app():
    app = Flask('watermark')
    AdminLTE(app)

    app.secret_key = 'LearnFlaskTheHardWay2017'
    login_manager.init_app(app)

    for bp in all_blueprints:
        import_module(bp.import_name)
        app.register_blueprint(bp)

    print(app.url_map)

    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
