#!/usr/bin/env python3
"""FIFOCache Module
"""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """BasicCache defines a basic caching system based on
       the First in first out (FIFO) algorithm
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
                discarded_key = self.cache_data.popitem(last=False)
                print(f'DISCARD: {discarded_key[0]}')
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key
        """
        if key:
            return self.cache_data.get(key, None)
