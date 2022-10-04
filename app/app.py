from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import environ

app = Flask(__name__)

load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

db.create_all()

from models import Todo

@app.route('/')
def home():
    todo_list = db.session.query(Todo).all()
    # return '<h1>Hello World!</h1>'
    return render_template("base.html", todo_list=todo_list)
