#!/usr/bin/env python3
from connection import Connection
from flask_restx import Api
from flask import Flask, Blueprint

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}

conn = Connection()
api_v1 = Blueprint("api", __name__, url_prefix="/api")
api = Api(api_v1, version="1.0", title="Secrets Manager",
          description="Secrets management simplified",
          authorizations=authorizations, security='apikey')
app = Flask(__name__)
app.register_blueprint(api_v1)


def abort_if_authorization_fail(token):
    """ Check if an API token is valid
    Args:
        token (str): API Token
    """
    if not conn.tokens.is_authorized(token):
        api.abort(403, "Not Authorized to access the requested resource")


# Import API Resources
# The below conditions prevents IDE auto-formatting
if True:
    from Api.resources.KV_resources import Engine_KV  # noqa: F401
