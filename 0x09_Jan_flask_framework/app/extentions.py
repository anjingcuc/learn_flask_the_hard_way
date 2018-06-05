# -*- coding: UTF-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy(use_native_unicode="UTF-8")
login_manager = LoginManager()
bcrypt = Bcrypt()
