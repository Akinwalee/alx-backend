#!usr/bin/env python3
"""
FIFO based caching module
"""
from base_caching import BaseCaching


class FifoCache(BaseCaching):
    """
    The class for FIFO based caching implementation
    """

    def put(self, key, item):
        """
        Put an item into the cache dict
        """

        if key and item:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = list(self.cache_data.keys())[-1]
                print(f"DISCARD: {last_key}")
                del self.cache_data[first_key]

            self.cache_data[key] = item

    def get(self, key):
        """
        Get a cache data by key
        """

        if not key or key not in self.cache_data.keys():
            return (None)

        return (self.cache_data[key])
