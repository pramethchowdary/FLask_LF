from flask import Flask, request, Response, session, redirect, url_for

app = Flask(__name__)

app.secret_key  = "keyyyyyyyy!"

@app.route("/",methods = ["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "prameth" and password == "Chow":
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid Cred Buddy!",mimetype="text/plain")
    return'''
    <h2> Login Page </h2>
    <form method = "POST">
    Username: <input type = "text" name = "username"><br>
    Password: <input type = "password" name = "password"><br>
    <input type = "submit" value = "Login">
    </forms>

'''
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
        <h1> Welcome {session["user"]}! You are loggedin</h1>
        <a href = {url_for("logout")}><button type = "button">Logout</button> </a>
        '''
    return redirect(url_for("login")) 

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


"""
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/contact",methods =["GET","POST"])
def contact():
    if request.method == "GET":
        return "Contact us at 522006"
    else:
        return "This page is under construction!"
"""