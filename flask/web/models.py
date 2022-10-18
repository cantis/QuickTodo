from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from web import db


class Todo(db.Model):
    '''Represents a todo item'''

    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    is_complete = Column(Integer, default=0)
    date_created = Column(DateTime, default=datetime.today())
    notes = relationship("Note", backref="todo")


class Note(db.Model):
    '''Represents a note'''

    __tablename__ = 'note'
    id = Column(Integer, primary_key=True)

    title = Column(String(100))
    content = Column(String(1000))
    date_created = Column(DateTime, default=datetime.today())
    todo_id = Column(Integer, db.ForeignKey('todo.id'))