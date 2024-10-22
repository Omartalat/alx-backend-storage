#!/usr/bin/env python3
"""
Inserts a new document in a MongoDB collection.

Args:
    mongo_collection (pymongo.collection.Collection): The MongoDB collection to insert the document into.
    **kwargs: Arbitrary keyword arguments representing the fields and values of the document to be inserted.

Returns:
    ObjectId: The ID of the inserted document.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection.
    Args:
        mongo_collection: The MongoDB collection instance.
        **kwargs: Arbitrary keyword arguments representing the fields and values of the document to be inserted.
    Returns:
        The ID of the inserted document.
    """
    new_collection = mongo_collection.insert_one(kwargs)
    return new_collection.inserted_id
