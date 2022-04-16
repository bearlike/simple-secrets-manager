#!/usr/bin/env python3
from Api.api import app
from flask import jsonify


@app.errorhandler(404)
def not_found(e):
    return jsonify(error="Resource not found"), 404


@app.errorhandler(Exception)
def server_error(e):
    app.logger.exception(e)
    return jsonify(error="Server error. Contact administrator"), 500
