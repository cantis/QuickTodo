from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime

from web import db


class Todo(db.Model):
    '''Represents a todo item'''

    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    is_complete = Column(Integer, default=0)
    date_created = Column(DateTime, default=datetime.today())


def init_db() -> None:
    db.create_all()
