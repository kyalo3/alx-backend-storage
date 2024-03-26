#!/usr/bin/env python3
"""function that inserts all documents in a collection """


def insert_school(mongo_collection, **kwargs):
    """ return an empty list if no doc is present """
    return mongo_collection.insert_one(kwargs).inserted_id
