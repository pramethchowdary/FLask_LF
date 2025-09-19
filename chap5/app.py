from flask import Flask, render_template, request,redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for("feedback"))


@app.route("/feedback",methods=["GET","POST"])
def feedback():
    if request.method == "POST":
        username = request.form.get("username")
        message = request.form.get("message")
        
        return render_template("thankyou.html",user = username,message=message )
    return render_template("feedback.html")