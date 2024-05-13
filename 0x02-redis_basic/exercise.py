#!/usr/bin/env python3

import redis
import uuid
from typing import Union
"""
Create a Cache class
"""


class Cache:
    """
    The __init__ method, store an instance of the Redis
    client as a private variable
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        This method that takes a data argument and returns a string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
