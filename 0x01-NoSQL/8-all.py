#!/usr/bin/env python3
"""
Lists all documents in a MongoDB collection.

Args:
    mongo_collection (pymongo.collection.Collection): The MongoDB collection to query.

Returns:
    pymongo.cursor.Cursor: A cursor to the documents in the collection.
"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.
    Args:
        mongo_collection: A pymongo collection object.
    Returns:
        A cursor to the documents in the collection.
    """
    return mongo_collection.find()
