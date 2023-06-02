"""General use functions."""
from flask import abort, render_template, session, redirect, url_for, jsonify
from hackday.model import DB

def return_forbidden():
    """Return forbidden message."""
    context = {
        "message": "Forbidden",
        "status_code": 403
    }
    return jsonify(**context), 403


def return_not_found():
    """Return not found message."""
    context = {
        "message": "Not Found",
        "status_code": 404
    }
    return jsonify(**context)


def return_bad_request():
    """Return forbidden message."""
    context = {
        "message": "Bad Request",
        "status_code": 400
    }
    return jsonify(**context)

def lower_words(s):
    """Captalizes each word in a string s."""
    return ' '.join([word.lower() for word in s.split()])