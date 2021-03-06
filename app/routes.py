from app import app
from flask import render_template, request

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Bea'}
    posts = [
        {'author': {'username': 'Beatriz'}, 'body': "Olá da Bea"},
        {'author': {'username': 'Fernando'}, 'body': "Olá!"}
    ]
    return render_template("index.html", user=user, posts=posts)

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print(request.values.get("user"), request.values.get("pass", request.values.get("remember")))
    return render_template("login.html", title="Login")