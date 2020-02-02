from app import db
from app.inc import Dao


class Course(db.Model, Dao):

    __tablename__ = 'course'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    summary = db.Column(db.Text, nullable=False)
    open = db.Column(db.Boolean, nullable=False, default=False)
    access = db.Column(db.SmallInteger, nullable=False)
    cost = db.Column(db.Float, nullable=False)
    open_at = db.Column(db.Date, nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __init__(name, summary, open, access, cost, open_at, active, owner_id, id=None):
        self.id = id
        self.name = name
        self.summary = summary
        self.open = open
        self.access = access
        self.cost = cost
        self.open_at = open_at
        self.active = active
        self.owner_id = owner_id


    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'summary': self.summary,
            'open': self.open,
            'access': self.access,
            'cost': self.cost,
            'open_at': self.open_at,
            'active': self.active,
            'owner_id': self.owner_id,
        }
