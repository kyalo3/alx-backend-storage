#!/usr/bin/env python3
"""function that lists all documents in a collection """


def list_all(mongo_collection):
    """ return an empty list if no doc is present """
    return mongo_collection.find()
