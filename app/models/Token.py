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
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __init__(self, action, user_id, token=None, expires_at=None, id=None):
        self.id = id
        self.action = action
        self.user_id = user_id
        self.token = token if token else token_urlsafe(16)
        self.expires_at = expires_at if expires_at else datetime.now() + timedelta(days=1)


    def as_dict(self):
        return {
            'id': self.id,
            'token': self.token,
            'expires_at': self.expires_at,
            'action': self.action,
            'user_id': self.user_id
        }
