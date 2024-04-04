#!/usr/bin/env python3
"""MRUCache Module
"""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """BasicCache defines a basic caching system based on
       the More Recently Used (MRU) algorithm
    """
    def __init__(self):
        """Instance initializer
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add or update an item in the cache according to the MRU policy."""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                recent = self.cache_data.popitem(last=True)
                print(f'DISCARD: {recent[0]}')
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key
        """
        if key and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
