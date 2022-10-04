from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime

from web import db


class Todo(db.Model):
    '''Represents a todo item'''

    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    complete = Column(Integer, default=0)
    date_created = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


def init_db():
    db.create_all()
