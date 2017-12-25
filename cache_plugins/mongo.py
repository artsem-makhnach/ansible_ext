
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

# moved actual classes to __init__ kept here for backward compat with 3rd parties
from ansible.plugins.cache import BaseCacheModule, BaseFileCacheModule

import pymongo.errors as errors
import pymongo
import json


class CacheModule(BaseCacheModule):
    def __init__(self, *args, **kwargs):
        self._cache = {}

    def get(self, key):
        try:
            client = pymongo.MongoClient('127.0.0.1', 27017)
            my_db = client.my_db
            facts = my_db.facts
            facts.insert({"facts": format(json.dumps(self._cache))})
            return self._cache.get(key)
        except errors.ConnectionFailure:
            return "No connection with DB"

    def set(self, key, value):
        self._cache[key] = value

    def keys(self):
        return self._cache.keys()

    def contains(self, key):
        return key in self._cache

    def delete(self, key):
        del self._cache[key]

    def flush(self):
        self._cache = {}

    def copy(self):
        return self._cache.copy()

    def __getstate__(self):
        return self.copy()

    def __setstate__(self, data):
        self._cache = data
