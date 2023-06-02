"""General use functions."""
from flask import jsonify

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

def calculate_average_size(total_size, num_items):
    """Average size of data in the appropriate KB, MB or GB"""
    
    # Check if empty
    if num_items == 0:
        return "0"
    
    average_size = total_size / num_items
    # Determine the appropriate unit based on the magnitude of the average size
    if average_size < 1024:
        unit = "KB"
    elif average_size < 1024 ** 2:
        unit = "MB"
        average_size /= 1024
    else:
        unit = "GB"
        average_size /= 1024 ** 2

    # Format the average size with two decimal places
    average_size_formatted = "{:.2f}".format(average_size)

    return f"{average_size_formatted} {unit}"