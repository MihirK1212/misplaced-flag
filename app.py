from flask import Flask, render_template, request,redirect  , jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from werkzeug.utils import redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///flag.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Flag(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    flag = db.Column(db.String(500),nullable=False)
    pole = db.Column(db.String(500),nullable=False)

    def __repr__(self) -> str:
        return f"FlagTable"

db.create_all()

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/get_flag", methods=['GET','POST'])
def input():
    if request.method == 'POST':
        request_type = request.form['request_type']

        res = Flag.query.all()[0]
        res = res.flag if request_type=='flag' else res.pole

        if request_type == 'pole':
            return jsonify({"pole":res})
        else:
            return jsonify({"message":f"flag{res}"})



if __name__ == "__main__":
     app.run(debug=True,port=8000)
