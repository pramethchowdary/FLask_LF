from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)
valid_cred = {
    'admin': 'dow',
    'dev':'sick',
    'hack':'you_fool'
}
@app.route('/')
def home():
    return render_template("forms.html")

@app.route('/submit',methods =["POST"])
def submit():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username in valid_cred and password == valid_cred[username]:
            return redirect(url_for("welcome"))
        else:
            return f"""<h2>You are a Scum Bagg!<h2>
                <a href ={url_for("home")}><h3>Try again!<h3></a>
            """
    return redirect(url_for("home"))

@app.route('/welcome')
def welcome():
    return '''
<h2> Welcome home!</h2>
'''