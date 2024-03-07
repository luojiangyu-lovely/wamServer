from functools import lru_cache

from functools import lru_cache
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["admin"]
counters = mydb["counters"]


def getNextValue(user_Name):
    ret = counters.find_one_and_update({"_id": user_Name},
                                       {"$inc": {
                                           "sequence_value": 1
                                       }},
                                       projection={
                                           'sequence_value': True,
                                           '_id': False
                                       })
    return ret['sequence_value']