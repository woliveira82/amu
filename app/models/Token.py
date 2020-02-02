from app import db
from app.inc import Dao


class Tokens(db.Model, Dao):
    
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(32), unique=True)
    expires_at = db.Column(db.Date, nullable=False)
    action = db.Column(db.SmallInteger, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __init__(token, expires_at, action, user_id, id=None):
        self.id = id
        self.token = token
        self.expires_at = expires_at
        self.action = action
        self.user_id = user_id


    def as_dict(self):
        return {
            'id': self.id,
            'token': self.token,
            'expires_at': self.expires_at,
            'action': self.action,
            'user_id': self.user_id
        }


    @property
    def id(self):
        return self.id

    
    @id.setter
    def id(self, id):
        self.id = id


    @property
    def token(self):
        return self.token

    
    @token.setter
    def token(self, token):
        self.token = token


    @property
    def expires_at(self):
        return self.expires_at

    
    @expires_at.setter
    def expires_at(self, expires_at):
        self.expires_at = expires_at


    @property
    def action(self):
        return self.action

    
    @action.setter
    def action(self, action):
        self.action = action


    @property
    def user_id(self):
        return self.user_id

    
    @user_id.setter
    def user_id(self, user_id):
        self.user_id = user_id
