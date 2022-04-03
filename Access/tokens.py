#!/usr/bin/env python3
""" Token authentication for Secrets Manager
"""
# TODO: Max TTL, Access Control

from bson.timestamp import Timestamp
import datetime as dt
import secrets


class Tokens:
    def __init__(self, token_auth_col):
        """ API token operations
        Args:
            token_auth_col (pymongo.collection.Collection)
        """
        # * Create unique index on 'path' for secrets_manager_auth.tokens
        # * db.tokens.createIndex( { "token": 1 }, { unique: true } )
        self._tokens = token_auth_col

    def generate(self, max_ttl=15811200):
        """ Generates an API token
        Args:
            max_ttl (int, optional): Maximum TTL for generated token in seconds
                    Defaults to 6 months or 15811200 seconds.
        Returns:
            dict : Dictionary with operation status and an API token
        """
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
        """ Check if a given token is valid
        Args:
            token (str): API token
        Returns:
            bool: True for valid tokens and False otherwise.
        """
        finder = self._tokens.find_one({"token": token})
        # Return False, if token is not found
        if not finder:
            return False
        # Return True, if token is found
        # TODO: Check for Max TTL
        return True

    def renew(self):
        pass
