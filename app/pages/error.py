
from flask import render_template
from app import app

from faker import Faker

@app.route("/error", methods = ["GET"])
def Error():
    _faker = Faker()
    _loram_ipsum = _faker.paragraph(nb_sentences=10)
    return render_template("error.html", loram_ipsum = _loram_ipsum)
