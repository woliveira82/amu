from app import db
from app.inc import Dao


class Progress(db.Model, Dao):

    __tablename__ = 'progress'
    
    id = db.Column(db.Integer, primary_key=True)
    participation_id = db.Column(db.Integer, db.ForeignKey('participation.id'), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=False)
    finished_at = db.Column(db.DateTime, default=None)


    def __init__(self, user_id, course_id, bought_at, started_at, last_participation, id=None):
        self.id = id
        self.participation_id = participation_id
        self.lesson_id = lesson_id
        self.finished_at = finished_at


    def as_dict(self):
        return {
            'id': self.id,
            'participation_id': self.participation_id,
            'lesson_id': self.lesson_id,
            'finished_at': self.finished_at,
        }
