#!/usr/bin/env python3
"""function that filters school by topics"""


def schools_by__topic(mongo_collection, topic):
    """ filter the schools by topic """
    return mongo_collection.find({"topics": topic})
