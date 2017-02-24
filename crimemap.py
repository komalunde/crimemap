import string
import datetime
import dateparser
import json
from flask import Flask, url_for, redirect
from flask import render_template
from flask import request
import db_config
if db_config.test:
    from mockdbhelper import MockDBHelper as DBHelper
else:
    from dbhelper import DBHelper

categories = ['mugging','break_in']

app = Flask(__name__)
DB = DBHelper()

@app.route("/")
def home(error_message=None):
    crimes = DB.get_all_crimes()
    crimes = json.dumps(crimes)
    return render_template("home.html", crimes=crimes,categories=categories,error_message=error_message)

@app.route("/submitcrime", methods=['POST'])
def submitcrime():
    category = request.form.get("category")
    if category not in categories:
            return home()
    try:
        latitude = float(request.form.get("latitude"))
        longitude = float(request.form.get("longitude"))
    except ValueError:
            return home(error_message="Invalid lat long")

    date = format_date(request.form.get("date"))
    if not date:
            return home(error_message="Invalid date. please use yyyy-mm-dd format")

    description = sanitize_string(request.form.get("description"))
    DB.add_crime(category,date,latitude,longitude, description)
    return home()

def format_date(userdate):
    date = dateparser.parse(userdate)
    try:
        return  datetime.datetime.strftime(date, "%Y-%m-%d")
    except TypeError:
        return None

def sanitize_string(userinput):
    whitelist = string.letters + string.digits + " !?$.,;:-'()&"
    return filter(lambda x: x in whitelist,userinput)

if __name__== '__main__':
    app.run(port=5000,debug=True)
