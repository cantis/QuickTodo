from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    # return render_template('home.html')
    return '<h1>Hello World!</h1>'