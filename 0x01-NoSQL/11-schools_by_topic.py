#!/usr/bin/env python3
"""function that filters school by topics"""


def schools_by__topic(mongo_collection, topics):
    """ filter the schools by topic """
    return mongo_collection.find({"topics": topic})
