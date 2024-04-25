
from flask import render_template, request, redirect, url_for, session
from app import app

@app.route("/search_sql", methods = ["GET","POST"])
def Search_SQL():
    session["prev_search"] = ""

    if request.method == "POST":
        _query_condition = request.form["query_condition"]
        return redirect(url_for("SearchResults", query_condition = _query_condition))
    else:
        return render_template("search_sql.html")