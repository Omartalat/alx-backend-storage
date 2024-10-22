#!/usr/bin/env python3
"""
Updates the topics of a document in a MongoDB collection based on the name.

Args:
    mongo_collection (pymongo.collection.Collection): The MongoDB collection instance.
    name (str): The name of the school document to update.
    topics (list): The list of topics to set for the school document.

Returns:
    None
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a document in a MongoDB collection based on the name.
    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection to update.
        name (str): The name of the document to update.
        topics (list): The list of topics to set for the document.
    Returns:
        None
    """
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
