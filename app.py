#!/usr/bin/env python3

from flask_restx import fields, Api, Resource
from flask import Flask, Blueprint
from connection import Connection
import logging
import os
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(filename='secrets_manager.log',
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.WARNING)

conn = Connection()
api_v1 = Blueprint("api", __name__, url_prefix="/api")
api = Api(api_v1, version="1.0", title="Secrets Manager",
          description="Secrets management simplified",)
kv_ns = api.namespace(
    name="kv",
    description="Key-Value (kv) engine is used to store arbitrary secrets"
)

kv_model = api.model(
    "Engine_KV", {
        "path": fields.String(
            required=True,
            description="Path to the kv datastore"),
        "key": fields.String(
            required=True,
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
        "value": "Secret (value) for the corresponding Key (index) in Path",
    }
)
class Engine_KV(Resource):
    """Key-Value API operations"""

    @api.doc(description="Add a kv to a path", parser=kv_parser)
    @api.marshal_with(kv_model)
    def post(self, path, key):
        """Add a new kv to a path"""
        args = kv_parser.parse_args()
        return conn.kv.add(path, key, args['value'])

    @api.doc(description="Return a kv from a path")
    @api.marshal_with(kv_model)
    def get(self, path, key):
        """Fetch a given kv from a path"""
        return conn.kv.get(path, key)

    @api.doc(
        description="Delete a kv from a path",
        responses={204: "Secrets deleted"}
    )
    def delete(self, path, key):
        """Delete a given kv"""
        return conn.kv.delete(path, key)

    @api.doc(description="Update a kv in a path", parser=kv_parser)
    @api.marshal_with(kv_model)
    def put(self, path, key):
        """Update a given resource"""
        args = kv_parser.parse_args()
        return conn.kv.update(path, key, args['value'])


if __name__ == "__main__":
    os.system("clear")
    app = Flask(__name__)
    app.register_blueprint(api_v1)
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)
