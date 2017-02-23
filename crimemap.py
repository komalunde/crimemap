
from flask import Flask
from flask import render_template
from flask import request
import db_config
if db_config.test:
    from mockdbhelper import MockDBHelper as DBHelper
else:
    from dbhelper import DBHelper


app = Flask(__name__)
DB = DBHelper()

@app.route("/")
def home():
    try:
        data = DB.get_all_inputs()
    except Exception as e:
        print e
        data = None
    return render_template("home.html", data=data)


@app.route("/add",methods=["POST"])
def add():
    try:
        data = ['1', '2', '12-2-2017', 'sd', request.form.get("userinput")]
        DB.add_input(data)
    except Exception as e:
        print e
    return home()

@app.route("/clear")
def clear():
    try:
        DB.clear_all()
    except Exception as e:
        print e
    return home()

if __name__== '__main__':
    app.run(port=5000,debug=True)
