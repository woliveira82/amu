from app import db
from app.inc import Dao
from secrets import token_urlsafe
from datetime import datetime, timedelta


class Token(db.Model, Dao):

    __tablename__ = 'token'
    
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(32), unique=True, nullable=False)
    expires_at = db.Column(db.DateTime, nullable=True)
    action = db.Column(db.SmallInteger, nullable=False)
    password = db.Column(db.String(64), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __init__(self, action, user_id, token=None, expires_at=None, password=None, id=None):
        self.id = id
        self.token = token if token else token_urlsafe(16)
        self.expires_at = datetime.now() + timedelta(days=1) if not expires_at and action == 2 else expires_at
        self.action = action
        self.password = password
        self.user_id = user_id


    def as_dict(self):
        return {
            'id': self.id,
            'token': self.token,
            'expires_at': self.expires_at,
            'action': self.action,
            'password': self.password,
            'user_id': self.user_id,
        }
