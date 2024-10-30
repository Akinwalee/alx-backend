#!/usr/bin/env python3
"""
Least Recentky Used caching
"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRU Caching
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add key, item pair to cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.order.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
        Retrieve item based on key
        """
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
