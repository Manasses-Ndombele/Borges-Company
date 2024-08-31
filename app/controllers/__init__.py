from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/solutions/')
def solutions():
    return render_template('solutions.html')

@app.route('/projects/')
def projects():
    return render_template('projects.html')

@app.route('/support/')
def support():
    return render_template('support.html')

@app.route('/about/')
def about():
    return render_template('about.html')
