from flask import Blueprint, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import environ

from web import db
from web.models import Todo

# blueprint
bp = Blueprint('home', __name__, template_folder='templates', static_folder='static')


@bp.route('/', methods=['GET'])
def index():
    todo_list = db.session.query(Todo).all()
    return render_template('home.html', todo_list=todo_list)


@bp.route('/add', methods=['GET', 'POST'])
def add():
    title = request.form.get('todoTitle')
    new_todo = Todo(title=title, is_complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('home.index'))


@bp.route('/update/<int:todo_id>', methods=['GET', 'POST'])
def update(todo_id):
    todo = db.session.query(Todo).filter_by(id=todo_id).first()
    todo.is_complete = not todo.is_complete
    db.session.commit()
    return redirect(url_for('home.index'))


@bp.route('/delete/<int:todo_id>', methods=['GET', 'POST'])
def delete(todo_id):
    todo = db.session.query(Todo).filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('home.index'))
