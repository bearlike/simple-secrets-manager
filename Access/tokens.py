#!/usr/bin/env python3
""" Token authentication for Secrets Manager
"""
# TODO: Max TTL, Access Control

import pymongo
from bson.timestamp import Timestamp
import datetime as dt
import secrets


class Tokens:
    def __init__(self, token_auth_col):
        """ Class 
        Args:
            token_auth_col (pymongo.collection.Collection)
        """
        # * Create unique index on 'path' for secrets_manager_auth.tokens
        # * db.tokens.createIndex( { "token": 1 }, { unique: true } )
        self._tokens = token_auth_col

    def generate(self):
        token = secrets.token_hex(32)
        data = {
            "token": token,
            "generated_on": Timestamp(int(dt.datetime.today().timestamp()), 1),
        }
        _ = self._tokens.insert_one(data)
        status = dict(**{"token": token}, **{"status": "OK"})
        return status

    def revoke(self, token):
        finder = self._tokens.find_one({"token": token})
        if not finder:
            result = {"status": "Path not found"}
        else:
            _ = self._tokens.delete_one({"token": token})
            result = {"status": "OK"}
        return result

    def is_authorized(self, token):
        finder = self._tokens.find_one({"token": token})
        # Return False, if token is not found
        if not finder:
            return False
        # Return False, if token is found
        return True

    def renew(self):
        pass
