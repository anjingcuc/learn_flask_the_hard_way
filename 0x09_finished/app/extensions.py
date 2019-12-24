# -*- coding: UTF-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


db = SQLAlchemy(use_native_unicode="UTF-8")
login_manager = LoginManager()
bcrypt = Bcrypt()
migrate = Migrate()
marshmallow = Marshmallow()
