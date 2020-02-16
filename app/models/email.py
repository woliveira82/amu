from datetime import datetime

from app import db
from app.inc import Dao
from datetime import datetime


class Email(db.Model, Dao):

    __tablename__ = 'email'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    inserted_at = db.Column(db.DateTime, nullable=False)


    def __init__(self, email, inserted_at=None, id=None):
        self.id = id
        self.email = email
        self.inserted_at = inserted_at if inserted_at else datetime.now()


    def as_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'inserted_at': self.inserted_at,
        }
