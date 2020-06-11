from pymongo import MongoClient
from constants import URL


class MyMongo:
    def __init__(self, url, db_name):
        self.db = MongoClient(url)[db_name]

    def let_me_udpdate(self, collection, data, id):
        self.db[collection].update_one(
            {"_id": id},
            {"$set": data},
        )

    def let_me_insert(self, collection, data):
        self.db[collection].insert_one(data)

    def let_me_delete(self, collection, pointer):
        self.db[collection].delete_one(pointer)

    def let_me_find_one(self, collection, pointer):
        return self.db[collection].find_one(pointer)

    def let_me_find_all(self, collection, pointer):
        return self.db[collection].find(pointer)


db_obj = MyMongo(URL, "university")
