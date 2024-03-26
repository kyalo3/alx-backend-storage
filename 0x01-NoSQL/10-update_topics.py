#!/usr/bin/env python3
"""function that changes all topics of a school document in a collection """


def update_topics(mongo_collection, name, topics):
    """ return an empty list if no doc is present """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
