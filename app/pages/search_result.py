
from flask import render_template, request, jsonify, redirect, url_for
from app import app

from sql import DataObjQueries, QueryConditions
from dataClasses import SQLDataBook, AbsSQLObj

@app.route("/search_results", methods = ["GET"])
def SearchResults():
    try:
        _query_condition = request.args["query_condition"]
        if 1 < len(_query_condition.split(";")):
            return redirect(url_for('Error'))
        print("Search condition: %s" % (_query_condition))
    except:
        return redirect(url_for('Error'))

    _dq = DataObjQueries()
    _dict_list: list[dict] = _dq.fetch(SQLDataBook, _query_condition)

    headings = _get_book_headers()
    data = []
    for _dict in _dict_list:
        data.append([_capitalize_title(x) for x in _dict.values()])

    return render_template("search_results.html", headings=headings, data=data, result_count = len(data), query_condition = _query_condition)

def _get_book_headers():
    return [_capitalize_title(x) for x in AbsSQLObj.get_build_headers(SQLDataBook)[1:]]

def _capitalize_title(title:str) -> str:
    if type(title) is not str:
        return title
    
    title = title.replace("_", " ")
    if title.isupper():
        return title
    
    return title.capitalize()