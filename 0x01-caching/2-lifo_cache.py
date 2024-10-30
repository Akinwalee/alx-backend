#!usr/bin/env python3
"""
FIFO based caching module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """
    The class for FIFO based caching implementation
    """

    def __init__(self):
        """
        Init
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Put an item into the cache dict
        """

        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key, v = self.cache_data.popitem(True)
                print(f"DISCARD: {first_key}")

    def get(self, key):
        """
        Get a cache data by key
        """

        if not key or key not in self.cache_data.keys():
            return (None)

        return (self.cache_data[key])
