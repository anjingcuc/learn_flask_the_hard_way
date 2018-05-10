# -*- coding: UTF-8 -*-
from app.application import create_app

from app.extentions import db

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

if __name__ == '__main__':
    flask_app = create_app()

    migrate = Migrate(flask_app, db)
    manager = Manager(flask_app)
    manager.add_command('db', MigrateCommand)
    manager.run()