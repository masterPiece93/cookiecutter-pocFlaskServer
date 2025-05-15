"""
This is where we will
"""

from flask import (
    Blueprint,
    jsonify
)

sample_api_bp = Blueprint(
    'sample_api',
    __name__,
    url_prefix='/'
)

@sample_api_bp.route('/sample-route', methods=['GET'])
def sample_route():
    return jsonify({"message": "this is a non-versioned sample api"})
