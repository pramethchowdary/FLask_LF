from flask import Flask,render_template

app = Flask(__name__)
Sname = "prameth"
Smarks = 90
Ssub = ['Computer','java','ecs']
@app.route('/')
def home():
    Istop = False
    if(Smarks>85):
        Istop = True
    return render_template('profile.html',name='Prameth',IsTopper = Istop,subjects = Ssub)