"""
This module defines a Flask application that provides an API for interacting with data.
"""

import json
from flask import Flask, make_response
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found(error):
    """
    JSON 404 page
    """
    response_dict = {"error": "Not found"}
    response = make_response(json.dumps(response_dict, indent=4), 404)
    response.headers['Content-Type'] = 'application/json'
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    
