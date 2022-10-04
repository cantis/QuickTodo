from flask import Blueprint, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import environ

# blueprint
bp = Blueprint('home', __name__, template_folder='templates', static_folder='static')


@bp.route('/')
def index():
    return render_template('home.html')
