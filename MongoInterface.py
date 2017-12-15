from pymongo import MongoClient
import json


# Settings
DailyRateCollectionName = 'DailyRate'


class MongoInterface():
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['MyFinanceManager']

    def insert(self, instance, collection_name):
        if self.db:
            collection = self.db[collection_name]
            collection.save(instance.encode_to_json())

    def search(self, query, collection_name):
        ret = None
        if query:
            collection = self.db[collection_name]
            ret = collection.find(query) #'SchemeCode': '120644'

        return ret

