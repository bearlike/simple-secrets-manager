#!/usr/bin/env python3
""" User-Pass authentication for Secrets Manager
"""
from bson.timestamp import Timestamp
import datetime as dt
import secrets
from werkzeug.security import generate_password_hash, check_password_hash


class User_Pass:
    def __init__(self, userpass_auth_col):
        """ Userpass operations
        Args:
            userpass_auth_col (pymongo.collection.Collection)
        """
        # * Create unique index on 'username' for secrets_manager_auth.userpass
        # * db.userpass.createIndex( { "username": 1 }, { unique: true } )
        self._userpass = userpass_auth_col

    def register(self, username, password):
        """ Register a new user
        Args:
            username (str): Username
            password (str): Password
        Returns:
            dict : Dictionary with operation status
        """
        finder = self._userpass.find_one({"username": username})
        if not finder:
            password = generate_password_hash(password, method='sha256')
            data = {
                "username": username,
                "password": password,
                "added_on": Timestamp(int(dt.datetime.today().timestamp()), 1),
            }
            _ = self._userpass.insert_one(data)
            status = {"status": "OK"}
        else:
            status = {"status": "User already exist"}
        return status

    def remove(self, username):
        """ Deletes an existing user
        Args:
            username (str): Username
        Returns:
            dict : Dictionary with operation status
        """
        finder = self._userpass.find_one({"username": username})
        if not finder:
            result = {"status": "Username does not exist"}
        else:
            _ = self._userpass.delete_one({"username": username})
            result = {"status": "OK"}
        return result

    def is_authorized(self, username, password):
        """ Check if a userpass is valid
        Args:
            username (str): Username
            password (str): Password
        Returns:
            bool: True for valid userpass and False otherwise.
        """
        finder = self._userpass.find_one({"username": username})
        # Return False, if username is not found
        if not finder:
            return False
        # Return True, if userpass is valid
        return check_password_hash(finder["password"], password)
