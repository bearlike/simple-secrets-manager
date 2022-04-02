#!/usr/bin/env python3
import pymongo
import logging
import os


class _KV:
    def __init__(self, kv_col):
        """ KV stands for Key-Value collection
        Args:
            kv_col (pymongo.collection.Collection)
        """
        # * Create unique index on 'path' for the kv collection
        # * db.kv.createIndex( { "path": 1 }, { unique: true } )
        self._kv = kv_col

    def get(self, path, key):
        finder = self._kv.find_one({"path": path})
        if not finder:
            result = {"status": "Path not found"}
        elif key not in finder["data"].keys():
            result = {"status": f"Key not found in '{path}'"}
        else:
            result = {
                "value": finder["data"][key],
                "status": "OK"
            }
        result.update({
            "path": path,
            "key": key,
        })
        return result

    def add(self, path, key, value):
        finder = self._kv.find_one({"path": path})
        if finder is None:
            # Create Path
            finder = {
                "path": path,
                "data": dict(),
            }
            _ = self._kv.insert_one(finder)
        if key not in finder["data"].keys():
            # After Creating path, add kv
            self._kv.update_one(
                {"path": path}, {"$set": {f"data.{key}": value}})
            result = {"status": "success"}
        else:
            result = {"status": f"Key already exist in '{path}'"}
        result.update({
            "path": path,
            "key": key,
        })
        return result

    # TODO: delete kv from path
    def delete(self, path, key):
        return {
            "status": "Not Implemented yet"
        }

    # TODO: update kv from path
    def update(self, path, key, value):
        return {
            "status": "Not Implemented yet"
        }


class Connection:
    def __init__(self, database="secrets_manager"):
        if os.environ.get("CONNECTION_STRING") is None:
            logging.error("CONNECTION_STRING variable not found")
            exit(-1)
        # Create a connection using MongoClient.
        self._client = pymongo.MongoClient(os.environ["CONNECTION_STRING"])
        self._db = self._client[database]
        self.kv = _KV(self._db['kv'])
