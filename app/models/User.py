from app import db
from app.inc import Dao


class User(db.Model, Dao):

    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(64), nullable=False)
    deactivated_at = db.Column(db.Date, default=None)
    name = db.Column(db.String(256), nullable=False)
    last_name = db.Column(db.String(256))


    def __init__(self, email, password, deactivated_at, name, last_name, id=None):
        self.id = id
        self.email = email
        self.password = password
        self.deactivated_at = deactivated_at
        self.name = name     
        self.last_name = last_name


    def as_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'deactivated_at': self.deactivated_at,
            'name': self.name,
            'last_name': self.last_name,
        }
