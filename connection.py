#!/usr/bin/env python3
""" Brains for the Secrets Manager
"""
import pymongo
import logging
import os
from Engines.kv import Key_Value_Secrets as _KV


class Connection:
    def __init__(self, database="secrets_manager"):
        if os.environ.get("CONNECTION_STRING") is None:
            logging.error("CONNECTION_STRING variable not found")
            exit(-1)
        # Create a connection using MongoClient.
        self._client = pymongo.MongoClient(os.environ["CONNECTION_STRING"])
        self._db = self._client[database]
        self.kv = _KV(self._db['kv'])
