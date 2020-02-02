from app import db
from app.inc import Dao


class User(db.Model, Dao):
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.Stirng(128), nullable=False) # verificar tamanho do hash bcrypt
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


    @property
    def id(self):
        return self.id

    
    @id.setter
    def id(self, id):
        self.id = id


    @property
    def email(self):
        return self.email

    
    @email.setter
    def email(self, email):
        self.email = email


    @property
    def password(self):
        return self.password

    
    @password.setter
    def password(self, password):
        self.password = password


    @property
    def deactivated_at(self):
        return self.deactivated_at

    
    @deactivated_at.setter
    def deactivated_at(self, deactivated_at):
        self.deactivated_at = deactivated_at


    @property
    def name(self):
        return self.name

    
    @name.setter
    def name(self, name):
        self.name = name


    @property
    def last_name(self):
        return self.last_name

    
    @last_name.setter
    def last_name(self, last_name):
        self.last_name = last_name

