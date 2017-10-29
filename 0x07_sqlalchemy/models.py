from flask_login import UserMixin

from database import db


# user models
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64))
    password = db.Column(db.String(128))

    def verify_password(self, password):
        return self.password == password

    def __repr__(self):
        return '<User %r>' % self.username
