from datetime import datetime

from app.extensions import db


class Post(db.Model):
    __tablename__ = "posts"
    __table_args__ = {"useexisting": True, 'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text)
    created_time = db.Column(db.DateTime, default=datetime.now)
