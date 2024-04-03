#!/usr/bin/env python3
"""LIFOCache Module
"""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """BasicCache defines a basic caching system based on
       the Lats In First Out (LIFO) algorithm
    """
    def __init__(self):
        """Instance initializer
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache
        """
        if key is not None and item is not None:
            if (
                len(self.cache_data) >= BaseCaching.MAX_ITEMS
                and key not in self.cache_data.keys()
            ):
                discarded_key = self.cache_data.popitem()
                print(f'DISCARD: {discarded_key[0]}')
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key
        """
        if key:
            return self.cache_data.get(key, None)
