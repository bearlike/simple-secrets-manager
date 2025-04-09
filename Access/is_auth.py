#!/usr/bin/env python3
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from Api.api import conn, api

# Auth Init
userpass = HTTPBasicAuth()
token = HTTPTokenAuth(scheme="Bearer")

# TODO: error_handler


@token.verify_token
def abort_if_authorization_fail(token_to_check):
    """Check if an API token is valid
    Args:
        token_to_check (str): API Token
    """
    check, username = conn.tokens.is_authorized(token_to_check)
    if check:
        return username
    api.abort(401, "Not Authorized to access the requested resource")
    return None


@userpass.verify_password
def verify_userpass(username, password):
    if conn.userpass.is_authorized(username, password):
        return username
    api.abort(401, "Not Authorized to access the requested resource")
    return None
