#!/usr/bin/env python3
"""
Least Frequently Used caching
"""


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFU Caching class
    """

    def __init__(self):
        """
        Init
        """
        super().__init__()
        self.freq_map = {}
        self.usage_order = []
        self.min_freq = 0

    def put(self, key, item):
        """
        Add key, item to the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self._update_frequency(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            self._remove_lfu()

        self.cache_data[key] = item
        self.freq_map[key] = 1
        self.usage_order.append(key)
        self.min_freq = 1

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        self._update_frequency(key)
        return self.cache_data[key]

    def _update_frequency(self, key):
        """
        Update the frequency of the given key.
        """

        self.freq_map[key] += 1

        freq = self.freq_map[key]
        if freq > self.min_freq:
            self.min_freq = freq

    def _remove_lfu(self):
        """
        Remove the least frequently used item.
        """
        lfu_keys = [key for key, freq in self.freq_map.items() if freq == self.min_freq]

        lfu_key = None
        for key in self.usage_order:
            if key in lfu_keys:
                lfu_key = key
                break
        
        if lfu_key:
            del self.cache_data[lfu_key]
            del self.freq_map[lfu_key]
            self.usage_order.remove(lfu_key)
            print(f"DISCARD: {lfu_key}")

