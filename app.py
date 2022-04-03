#!/usr/bin/env python3

from flask_restx import fields, Api, Resource
from flask import Flask, Blueprint, request
from connection import Connection
import logging
import os
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(filename='secrets_manager.log',
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.WARNING)

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


def abort_if_authorization_fail(API_KEY):
    # TODO: Abort if API auth fail
    print("API_KEY:", API_KEY)


# KV Namespace
kv_ns = api.namespace(
    name="kv",
    description="Key-Value (kv) engine is used to store arbitrary secrets"
)

kv_model = api.model(
    "Engine_KV", {
        "path": fields.String(
            required=True, pattern="[a-zA-Z0-9_]+", min_length=1,
            description="Path to the kv datastore"),
        "key": fields.String(
            required=True, pattern="[a-zA-Z0-9_]+", min_length=1,
            description="Key (index) in path where a secret is stored"),
        "value": fields.String(
            required=True,
            description="Secret (value) for the corresponding Key in Path"),
        "status": fields.String(
            required=False,
            description="Operation Status"),
    }
)

kv_parser = api.parser()
kv_parser.add_argument(
    "value", type=str, required=True, location="form",
    help="Secret (value) for the corresponding Key (index) in Path"
)


@kv_ns.route("/<string:path>/<string:key>")
@api.doc(
    responses={404: "Path or kv not found"},
    params={
        "path": "Path to a kv store",
        "key": "Key (index) in path where a secret (value) is stored",
    }
)
class Engine_KV(Resource):
    """Key-Value API operations"""

    @api.doc(description="Update a kv in a path", parser=kv_parser)
    @api.marshal_with(kv_model)
    def put(self, path, key):
        """Update a given resource"""
        args = kv_parser.parse_args()
        API_KEY = request.headers.get('X-API-KEY', type=str, default=None)
        abort_if_authorization_fail(API_KEY)
        return conn.kv.update(path, key, args['value'])

    @api.doc(
        description="Delete a kv from a path",
        responses={204: "Secrets deleted"})
    def delete(self, path, key):
        """Delete a given kv"""
        API_KEY = request.headers.get('X-API-KEY', type=str, default=None)
        abort_if_authorization_fail(API_KEY)

        return conn.kv.delete(path, key)

    @api.doc(description="Add a kv to a path", parser=kv_parser)
    @api.marshal_with(kv_model)
    def post(self, path, key):
        """Add a new kv to a path"""
        args = kv_parser.parse_args()
        API_KEY = request.headers.get('X-API-KEY', type=str, default=None)
        abort_if_authorization_fail(API_KEY)

        return conn.kv.add(path, key, args['value'])

    @api.doc(description="Return a kv from a path")
    @api.marshal_with(kv_model)
    def get(self, path, key):
        """Fetch a given kv from a path"""
        API_KEY = request.headers.get('X-API-KEY', type=str, default=None)
        abort_if_authorization_fail(API_KEY)
        return conn.kv.get(path, key)


if __name__ == "__main__":
    os.system("cls")
    print("Reloading app...")
    app = Flask(__name__)
    app.register_blueprint(api_v1)
    app.run(host='0.0.0.0', port=os.environ.get("PORT", 5000),
            debug=True, use_reloader=True)
