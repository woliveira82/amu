from app import db
from app.inc import Dao


class Participation(db.Model, Dao):

    __tablename__ = 'participation'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    bought_at = db.Column(db.Date, default=None)
    started_at = db.Column(db.Date, default=None)
    last_participation = db.Column(db.Date)


    def __init__(self, user_id, course_id, bought_at, started_at, last_participation, id=None):
        self.id = id
        self.user_id = user_id
        self.course_id = course_id
        self.bought_at = bought_at
        self.started_at = started_at
        self.last_participation = last_participation


    def as_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'course_id': self.course_id,
            'bought_at': self.bought_at,
            'started_at': self.started_at,
            'last_participation': self.last_participation,
        }
