
from flask import render_template, request, redirect, url_for
from app import app

@app.route("/search_sql", methods = ["GET","POST"])
def Search_SQL():
    if request.method == "POST":
        _query_condition = request.form["query_condition"]
        return redirect(url_for("SearchResults", query_condition = _query_condition))
    else:
        return render_template("search_sql.html")