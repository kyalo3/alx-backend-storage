#!/usr/bin/env python3
"""function that inserts a new document in a collection """
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """ Iterate over all documents in the collection
    and append them to the list
    """
    for document in mongo_collection.find():
        all_docs.append(document)

    return _id
