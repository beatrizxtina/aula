from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Bea'}
    posts = [
        {'author': {'username': 'Beatriz'}, 'body': "Olá da Bea"},
        {'author': {'username': 'Fernando'}, 'body': "Olá!"}
    ]
    return render_template("index.html", user=user, posts=posts)