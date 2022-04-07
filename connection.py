#!/usr/bin/env python3
""" Brains for the Secrets Manager
"""
import pymongo
import logging
import os
# Secret Engines
from Engines.kv import Key_Value_Secrets as _KV
# Auth Methods
from Access.tokens import Tokens as _Tokens
from Access.userpass import User_Pass as _User_Pass


class Connection:
    def __init__(self):
        if os.environ.get("CONNECTION_STRING") is None:
            logging.error("CONNECTION_STRING variable not found")
            exit(-1)
        # Create a connection using MongoClient.
        self._client = pymongo.MongoClient(os.environ["CONNECTION_STRING"])
        self._data = self._client["secrets_manager_data"]
        self._auth = self._client["secrets_manager_auth"]
        # Secret Engines
        self.kv = _KV(self._data['kv'])
        # Auth Methods
        self.tokens = _Tokens(self._auth['tokens'])
        self.userpass = _User_Pass(self._auth['userpass'])
