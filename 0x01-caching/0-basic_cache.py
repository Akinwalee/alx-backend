#!/usr/bin/env python3
"""
Basic Caching module
"""
BaseCaching = __import__("base_caching.py").BaseCaching


class BasicCache(BaseCaching):
    """
    BaseCaching defines:
    - constants of the caching systems
    - where the data are stored (in a dictionary)
    """

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key and item:
            self.cace_data[key] = item

    def get(self, key):
        """
        Get an item with its key
        """
        if not key or key not in self.cache_data.keys():
            return (None)

        return (self.cach_data[key])
