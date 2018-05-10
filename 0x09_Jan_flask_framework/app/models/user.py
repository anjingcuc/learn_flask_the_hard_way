# -*- coding: UTF-8 -*-
from flask_login import UserMixin
from datetime import datetime

from app.extentions import db


# user models
class User(db.Model, UserMixin):
    __tablename__ = "user"
    __table_args__ = {"useexisting": True, 'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    email_confirmed = db.Column(db.Boolean)
    name = db.Column(db.String(100))
    role = db.Column(db.String(10))
    password = db.Column(db.String(100))
    created_time = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return "<User %r>" % self.name

    def check_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, password)

    def is_authenticated(self):
        return True

    def is_actice(self):
        return True

    def is_anonymous(self):
        return False
