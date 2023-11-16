# import flask
# print(flask.__version__)

from flask import Flask, render_template, request, redirect
from Classes import User, UsersContainerSingleton, Auth
import pyfiglet

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home_page():
    container = UsersContainerSingleton.get_instance()
    container.load_users()
    if request.method == 'POST' and "name" in request.form and "email" in request.form and "password" in request.form:
        # Register
        u = Auth.register(request.form["name"].strip(), request.form["email"].strip(), request.form["password"].strip())
        if u:
            return f"<pre>{pyfiglet.figlet_format("Hello "+u.name)}</pre>"
        else:
            return f"<pre>{pyfiglet.figlet_format("Sorry, Failed To Register")}</pre>"
    elif request.method == 'POST' and "email" in request.form and "password" in request.form:
        #Login
        u = Auth.login(request.form["email"].strip(), request.form["password"].strip())
        if u:
            return f"<pre>{pyfiglet.figlet_format("Welcome Back, "+u.name)}</pre>"
        else:
            return f"<pre>{pyfiglet.figlet_format("Sorry, Failed To Login")}</pre>"
    return render_template("home.html")

@app.route("/login")
def login_page():
    return render_template("login.html", title="Login")

@app.route("/register")
def register_page():
    return render_template("register.html", title="Register")

if __name__ == "__main__":
    app.run(debug=True, port=9000)