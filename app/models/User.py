from app import db
from app.inc import Dao
from . import Token
from datetime import datetime


class User(db.Model, Dao):

    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    deactivated_at = db.Column(db.DateTime, default=None)
    name = db.Column(db.String(256), nullable=False)
    last_name = db.Column(db.String(256))


    def __init__(self, email, password, name, last_name, active=False, deactivated_at=None, id=None):
        self.id = id
        self.email = email
        self.password = password
        self.active = active
        self.deactivated_at = deactivated_at
        self.name = name     
        self.last_name = last_name


    def as_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,
            'active': self.active,
            'deactivated_at': self.deactivated_at,
            'name': self.name,
            'last_name': self.last_name,
        }

    
    def create(self):
        super().create()
        
        token_data = {
            'action': 1,
            'user_id': self.id,
        }
        token = Token(**token_data)
        token.create()