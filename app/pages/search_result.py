
from flask import render_template, request, jsonify, redirect, url_for
from app import app

from sql import DataObjQueries, QueryConditions
from dataClasses import SQLDataBook, AbsSQLObj

@app.route("/search_results", methods = ["GET"])
def SearchResults():
    try:
        _condition = request.args["query_condition"]
        _condition = _condition.split(";")[0]
        print("Search condition: %s" % (_condition))
    except:
        return redirect(url_for('Error'))

    _dq = DataObjQueries()
    _dict_list: list[dict] = _dq.fetch(SQLDataBook, _condition)

    headings = _get_book_headers()
    data = []
    for _dict in _dict_list:
        data.append([_capitalize_title(x) for x in _dict.values()])

    return render_template("table.html", headings=headings, data=data)

def _get_book_headers():
    return [_capitalize_title(x) for x in AbsSQLObj.get_build_headers(SQLDataBook)[1:]]

def _capitalize_title(title:str) -> str:
    if type(title) is not str:
        return title
    
    title = title.replace("_", " ")
    if title.isupper():
        return title
    
    return title.capitalize()