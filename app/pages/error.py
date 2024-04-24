
from flask import render_template
from app import app

@app.route("/error", methods = ["GET"])
def Error():
    return render_template("error.html")
