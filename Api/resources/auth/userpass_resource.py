#!/usr/bin/env python3
# Userpass Authentication API Resource
from flask_restx import fields, Resource
from Api.api import api, conn

# Userpass Auth Namespace
userpass_ns = api.namespace(
    name="auth/userpass",
    description="Allows authentication using a username and password.",
)
userpass_model = api.model(
    "Auth Method - Userpass",
    {
        "username": fields.String(
            required=True,
            pattern="[a-fA-F0-9_]+",
            min_length=2,
            description="Username for userpass authentication",
        ),
        "password": fields.String(
            required=True,
            min_length=6,
            description="Password for userpass authentication",
        ),
        "status": fields.String(required=False, description="Operation Status"),
    },
)

# Userpass Arguments
# For deleting user
delete_userpass_parser = api.parser()
delete_userpass_parser.add_argument(
    "username",
    type=str,
    required=True,
    location="form",
    help="Username must already exist.",
)
# For adding new user
post_userpass_parser = api.parser()
post_userpass_parser.add_argument(
    "username",
    type=str,
    required=True,
    location="form",
    help="Username must atleast be 1 characters long",
)
post_userpass_parser.add_argument(
    "password",
    type=str,
    required=True,
    location="form",
    help="Password should satisfy policy",
)


@userpass_ns.route("/delete")
@api.doc(responses={}, params={})
class Auth_Userpass_delete(Resource):
    """Userpass operations"""

    @api.doc(
        description="Revoke a given user",
        responses={
            200: "User account removed",
            400: "User does not exist",
        },
        parser=delete_userpass_parser,
    )
    @api.marshal_with(userpass_model)
    def delete(self):
        """Revoke a given user"""
        args = delete_userpass_parser.parse_args()
        status, code = conn.userpass.remove(username=args["username"])
        if code != 200:
            api.abort(code, status)
        return status


@userpass_ns.route("/register")
@api.doc(responses={}, params={})
class Auth_Userpass_register(Resource):
    """Userpass operations"""

    @api.doc(
        description="Register new user.",
        responses={
            200: "User account created",
            400: "Invalid username or password",
        },
        parser=post_userpass_parser,
    )
    @api.marshal_with(userpass_model)
    def post(self):
        """Register new user"""
        # TODO: Support for root key to create new users
        args = post_userpass_parser.parse_args()
        _usr, _pass = args["username"], args["password"]
        status, code = conn.userpass.register(username=_usr, password=_pass)
        if code != 200:
            api.abort(code, status)
        return status
