# import flask
# print(flask.__version__)

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return "<h1>This is The Home Page</h1>"

@app.route("/login")
def login_page():
    return render_template("login.html", title="Login")

@app.route("/register")
def register_page():
    return "<h1>Register</h1>"

if __name__ == "__main__":
    app.run(debug=True, port=9000)