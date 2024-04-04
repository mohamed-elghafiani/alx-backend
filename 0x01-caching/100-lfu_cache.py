#!/usr/bin/env python3
"""LFUCache Module
"""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """BasicCache defines a basic caching system based on
       the Least Frequently Used (LFU) algorithm
    """
    def __init__(self):
        """Instance initializer
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequency = {}

    def put(self, key, item):
        """Add or update an item in the cache according to the LFU policy."""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
                self.frequency[key] += 1
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu = min(self.frequency, key=lambda k: self.frequency[k])
                print(f'DISCARD: {lfu}')
                del self.cache_data[lfu]
                del self.frequency[lfu]
            self.cache_data[key] = item
            self.frequency[key] = 1

    def get(self, key):
        """Get an item by key
        """
        if key and key in self.cache_data:
            self.cache_data.move_to_end(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
