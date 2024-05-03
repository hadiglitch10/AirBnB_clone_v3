#!/usr/bin/python3
"""
    This script starts a Flask web application
"""
from os import getenv
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from flasgger import Swagger 
from flasgger.utils import swag_from

app = Flask(__name__)
app.register_blueprint(app_views)



@app.teardown_appcontext
def teardown(self):
    """Remove the current SQLAlchemy session"""
    return storage.close()

if __name__ == "__main__":
    if getenv("HBNB_API_HOST"):
        host = getenv("HBNB_API_HOST")
    else:
        "0.0.0.0"
    
    if getenv("HBNB_API_PORT"):
        port = getenv("HBNB_API_PORT")
    else:
        5000
    app.run(host=host, port=port, threaded=True)
    