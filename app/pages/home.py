from flask import render_template, request, jsonify, redirect, url_for
from app import app

from sql import DataObjQueries, QueryConditions
from dataClasses import SQLDataBook, AbsSQLObj


@app.route("/", methods = ["GET","POST"])
def Home():
    return redirect(url_for('Search'))