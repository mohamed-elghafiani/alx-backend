#!/usr/bin/env python3
"""BasicCache Module
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache defines a basic caching system that inherit from BaseCaching
    """
    def __init__(self):
        """Instance initializer
        """
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key
        """
        if key:
            return self.cache_data.get(key, None)
