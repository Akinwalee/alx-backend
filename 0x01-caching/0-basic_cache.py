#!/usr/bin/env python3
"""
Basic Caching module
"""


class BaseCaching():
    """
    BaseCaching defines:
    - constants of the caching systems
    - where the data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """
        Initialize
        """

        self.cache_data = {}

    def print_caches(self):
        """
        Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

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
