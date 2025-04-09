#!/usr/bin/env python3
"""Database model for the Secrets Manager"""
import pymongo
import logging
import os
import sys

# Secret engines imports
from Engines.kv import Key_Value_Secrets as _KV

# Auth methods imports
from Access.tokens import Tokens as _Tokens
from Access.userpass import User_Pass as _User_Pass


class __connection:
    def __init__(self):
        if os.environ.get("CONNECTION_STRING") is None:
            logging.error("CONNECTION_STRING variable not found")
            sys.exit(-1)
        # Create a connection using MongoClient.
        self.__client = pymongo.MongoClient(os.environ["CONNECTION_STRING"])
        self.__data = self.__client["secrets_manager_data"]
        self.__auth = self.__client["secrets_manager_auth"]
        # Secret Engines
        self.kv = _KV(self.__data["kv"])
        # Auth Methods
        self.tokens = _Tokens(self.__auth["tokens"])
        self.userpass = _User_Pass(self.__auth["userpass"])


class Connection(__connection):
    # Singleton class to prevent multiple connections
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Connection, cls).__new__(cls)
        return cls.instance
