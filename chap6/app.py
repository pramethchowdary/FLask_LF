from flask import Flask,request,redirect,url_for,flash,render_template,session

app = Flask(__name__)
app.secret_key = "supper"

@app.route("/",methods=["GET","POST"])
def form():
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")
        if not name:
            flash("Name is compolsory!")
            return redirect(url_for("form"))
        elif not password:
            flash("for security resons you must fill the password!")
            return redirect(url_for("form"))
        flash(f"Thank you {name} your profile is created!")
        session["user"] = name
        return redirect(url_for("thankyou"))
    return render_template("form.html")

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html",user=session["user"])