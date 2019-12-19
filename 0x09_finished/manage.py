# -*- coding: UTF-8 -*-
from app.application import create_app


if __name__ == '__main__':
    flask_app = create_app()

    flask_app.run()