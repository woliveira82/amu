from app import db
from app.inc import Dao


class Lesson(db.Model, Dao):
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), unique=True)
    summary = db.Column(db.Text, nullable=False)
    updated_at = db.Column(db.Date, nullable=False)
    body = db.Column(db.Text, nullable=False)
    order = db.Column(db.SmallInteger, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)


    def __init__(title, summary, updated_at, body, order, course_id, id=None):
        self.id = id
        self.title = title
        self.summary = summary
        self.updated_at = updated_at
        self.body = body
        self.order = order
        self.course_id = course_id


    def as_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'summary': self.summary,
            'updated_at': self.updated_at,
            'body': self.body,
            'order': self.order,
            'course_id': self.course_id,
        }
