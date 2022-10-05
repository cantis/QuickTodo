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
