#!/usr/bin/env python3
"""function that lists all documents in a collection """
from pymongo import MongoClient


def list_all(mongo_collection):
    """ return an empty list if no doc is present """
    all_docs = []

    """ Iterate over all documents in the collection
    and append them to the list
    """
    for document in mongo_collection.find():
        all_docs.append(document)

    return all_docs
