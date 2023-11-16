# import flask
# print(flask.__version__)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_page():
    return "<h1>This is The Home Page</h1>"

@app.route("/login")
def login_page():
    return "<h1>Login</h1>"

@app.route("/register")
def register_page():
    return "<h1>Register</h1>"
