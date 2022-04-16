#!/usr/bin/env python3
from connection import Connection
from flask_restx import Api
from flask import Flask, Blueprint

authorizations = {
    "Token": {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    },
    "UserPass": {
        'type': 'basic'
    }
}


conn = Connection()
api_v1 = Blueprint("api", __name__, url_prefix="/api")
api = Api(api_v1, version="1.1.2", title="Simple Secrets Manager",
          description="Secrets management simplified",
          authorizations=authorizations)
app = Flask(__name__)
app.register_blueprint(api_v1)


# Import API Resources
# The below conditions prevents IDE auto-formatting
# skipcq: PYL-W0125
if True:
    # Secret Engines
    from Api.resources.secrets.kv_resource import Engine_KV  # noqa: F401
    from Api.resources.auth.tokens_resource import Auth_Tokens  # noqa: F401
    # Authentication methods
    from Api.resources.auth.userpass_resource \
        import Auth_Userpass_delete, Auth_Userpass_register  # noqa: F401
    # Handling HTTP Errors
    from Api.errors import errors  # noqa: F401
