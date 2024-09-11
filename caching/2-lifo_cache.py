#!/usr/bin/env python3
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching and is a caching system.
    Implements the LIFO (Last In, First Out) caching algorithm.
    """

    def __init__(self):
        """
        Initialize the class with the parent class's attributes.
        Calls the parent class's constructor using super().
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache using the LIFO algorithm.

        Args:
            key (str): The key for the cache item.
            item (any): The value associated with the key to store in the cache.

        If the cache exceeds BaseCaching.MAX_ITEMS, the last item added is discarded.
        If key or item is None, this method does nothing.

        Example:
            cache.put("A", "Apple")  # Adds 'Apple' to the cache with key 'A'.
        """
        if key is None or item is None:
            return  # Do nothing if key or item is None

        # Add the key-value pair to the cache
        self.cache_data[key] = item

        # Check if cache size exceeds the maximum allowed items
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # LIFO: Discard the last item put in cache
            last_key = list(self.cache_data.keys())[-2]  # Get the second last key
            del self.cache_data[last_key]  # Remove the second last item (LIFO behavior)
            print(f"DISCARD: {last_key}")  # Print the discarded key

    def get(self, key):
        """
        Retrieve an item from the cache using the key.

        Args:
            key (str): The key for the cache item.

        Returns:
            The value associated with the key, or None if the key is None or
            if the key does not exist in the cache.

        Example:
            value = cache.get("A")  # Retrieves the value associated with 'A' from the cache.
        """
        if key is None or key not in self.cache_data:
            return None  # Return None if key is None or does not exist in cache
        return self.cache_data.get(key)  # Return the value associated with the key

