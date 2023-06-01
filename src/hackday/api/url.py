"""REST API for Return API resource URLs."""
from flask import jsonify
import hackday

@hackday.app.route('/api/v1/', methods=['GET'])
def get_resources():
    """Return a JSON response of all API urls."""
    return jsonify(**{'url': '/api/v1/'})
