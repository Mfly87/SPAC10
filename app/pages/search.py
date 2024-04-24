from flask import render_template, request, jsonify, redirect, url_for
from app import app

from sql import QueryConditions
from dataClasses import SQLDataBook, AbsSQLObj

@app.route("/search", methods = ["GET","POST"])
def Search():
    if request.method == "POST":
        _query_column = request.form.get("query_column", None)
        _query_operator = request.form.get("query_operator", None)
        _query_value = request.form.get("query_value", None)

        _operator_func = QueryConditions.get_operator_func(_query_operator)
        _query_condition = _operator_func(_query_column.lower(),
                                          _query_value.lower()
                                          )

        return redirect(url_for("SearchResults", query_condition = _query_condition))
    else:
        _options = [(x, _capitalize_title(x)) for x in AbsSQLObj.get_build_headers(SQLDataBook)[1:]]
        return render_template("search.html", options = _options)



def _capitalize_title(title:str) -> str:
    if type(title) is not str:
        return title
    
    title = title.replace("_", " ")
    if title.isupper():
        return title
    
    return title
    #return title.capitalize()