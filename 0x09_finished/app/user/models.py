# -*- coding: UTF-8 -*-
from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property

from datetime import datetime

from app.extensions import db
from app.extensions import bcrypt

import enum


class UserRole(enum.Enum):
    ADMIN = 'Administrator'
    USERS = 'Normal users'


# user models
class User(db.Model, UserMixin):
    __tablename__ = "users"
    __table_args__ = {"useexisting": True, 'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    email_confirmed = db.Column(db.Boolean, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.Enum(UserRole), nullable=False)
    _password = db.Column(db.String(128), nullable=False)
    created_time = db.Column(db.DateTime, default=datetime.now)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    def is_correct_password(self, plaintext):
        return bcrypt.check_password_hash(self._password, plaintext)

    def __repr__(self):
        return "<User %r>" % self.name