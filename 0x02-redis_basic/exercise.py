#!/usr/bin/env python3
"""
A class used to represent a Cache using Redis.
Methods
-------
__init__():
    Initializes the Redis client and flushes the database.
store(data: str | bytes | int | float) -> uuid.UUID:
    Stores the given data in the Redis cache and returns a unique key.
"""
import redis
import uuid


class Cache:
    def __init__(self):
        """
        Initializes a new instance of the class.

        This constructor sets up a connection to the Redis server
        and flushes the
        database to ensure a clean state.

        Attributes:
            _redis (redis.Redis): The Redis client instance used to
            interact with the Redis server.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | bytes | int | float) -> uuid.UUID:
        """
        Store the given data in Redis and return a unique key.

        Args:
            data (str | bytes | int | float): The data to be stored in Redis.

        Returns:
            uuid.UUID: A unique key associated with the stored data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
