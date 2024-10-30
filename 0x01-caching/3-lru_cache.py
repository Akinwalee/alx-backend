#!/usr/bin/env python3
"""
Least Recentky Used caching
"""

from base_cache import BaseCaching

class LRUCache(BaseCaching):
    """
    LRU Cache
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add a key, item pair to the cache
        """

        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
        Retrieve an item with its key
        """

        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
