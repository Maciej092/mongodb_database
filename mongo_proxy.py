from pymongo import MongoClient
from constants import *


class MyMongo:
    def __init__(self):
        self.connection = MongoClient(host_name, port)
        self.db = self.connection['university']

    def let_me_insert(self, collection, data):
        """

        :param collection:
        :param data:
        :return:
        """
        self.db[collection].insert_one(data)
        return

    def let_me_udpdate(self, collection, data, id):
        """

        :param collection:
        :param data:
        :param id:
        :return:
        """
        self.db[collection].update_one({"_id": id}, {"$set": data})

    def let_me_find_one(self, collection, pointer):
        """

        :param collection:
        :param pointer:
        :return:
        """
        return self.db[collection].find_one(pointer)

    def let_me_find_all(self, collection, pointer):
        """

        :param collection:
        :param pointer:
        :return:
        """
        return self.db[collection].find(pointer)

    def let_me_delete(self, collection, pointer):
        """

        :param collection:
        :param pointer:
        :return:
        """
        self.db[collection].delete_one(pointer)





