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
    def __init__(self):
        """
        Initialize
        """
        self.cache_data = {}
        super().__init__(self)

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item with its key
        """
        if not key or key not in self.cache_data.keys():
            return (None)

        return (self.cache_data[key])
