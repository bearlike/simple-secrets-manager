#!/usr/bin/env python3
""" KV (Key-Value) Secret Engine for Secrets Manager
"""
import re


class Key_Value_Secrets:
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
        pattern = "[a-zA-Z0-9_]+"
        if not (re.fullmatch(pattern, key) and re.fullmatch(pattern, path)):
            return {"status": f"Key and/or Path does not match {pattern}"}
        finder = self._kv.find_one({"path": path})
        if finder is None:
            # Create a Path where kv(s) goes into
            finder = {
                "path": path,
                "data": {},
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

    def delete(self, path, key):
        finder = self._kv.find_one({"path": path})
        if not finder:
            result = {"status": "Path not found"}
        elif key not in finder["data"].keys():
            result = {"status": f"Key not found in '{path}'"}
        else:
            self._kv.update_one(
                {"path": path}, {"$unset": {f"data.{key}": 1}})
            # TODO: Delete document if path has no kv(s)
            result = {"status": "OK"}
        result.update({
            "path": path,
            "key": key,
        })
        return result

    def update(self, path, key, value):
        finder = self._kv.find_one({"path": path})
        if not finder:
            result = {"status": "Path not found"}
        elif key not in finder["data"].keys():
            result = {"status": f"Key not found in '{path}'"}
        else:
            self._kv.update_one(
                {"path": path}, {"$set": {f"data.{key}": value}})
            result = {"status": "OK"}
        result.update({
            "path": path,
            "key": key,
        })
        return result
