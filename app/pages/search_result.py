from flask import render_template, request, jsonify, redirect, url_for, Request, session
from app import app

from sql import DataObjQueries, QueryConditions
from dataClasses import SQLDataBook, AbsSQLObj

@app.route("/search_results", methods = ["GET", "POST"])
def SearchResults():

    _query_condition = request.args.get("query_condition", None)

    if request.method == "POST" and session["prev_search"]:
        _query_condition = session["prev_search"]
    else:
        session["prev_search"] = ""

    if _query_condition is None:
        return redirect(url_for('Error'))
    
    _query_joiner = request.form.get("query_joiner", None)
    if _query_joiner is not None:
        _query_column = request.form.get("query_column", None)
        _query_operator = request.form.get("query_operator", None)
        _query_value = request.form.get("query_value", None)

        _operator_func = QueryConditions.get_operator_func(_query_operator)
        _extra_condition = _operator_func(_query_column.lower(), _query_value.lower() )
        _conditions = [_query_condition, _extra_condition]
        _query_condition = QueryConditions.qry_or(_conditions) if _query_joiner == "OR" else QueryConditions.qry_and(_conditions)

    try:
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

    _options = _options = [(x, _capitalize_title(x)) for x in AbsSQLObj.get_build_headers(SQLDataBook)[1:]]
    session["prev_search"] = _query_condition

    return render_template("search_results.html", headings=headings, data=data, options = _options, result_count = len(data), query_condition = _query_condition)



def _get_book_headers():
    return [_capitalize_title(x) for x in AbsSQLObj.get_build_headers(SQLDataBook)[1:]]

def _capitalize_title(title:str) -> str:
    if type(title) is not str:
        return title
    
    title = title.replace("_", " ")
    if title.isupper():
        return title
    
    return title.capitalize()