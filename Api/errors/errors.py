#!/usr/bin/env python3
from Api.api import app
from flask import jsonify, request

@app.errorhandler(404)
def not_found(e):
    return jsonify(error="Resource not found"), 404
