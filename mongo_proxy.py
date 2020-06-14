from pymongo import MongoClient
from constants import DataBase as DbModule
import traceback as TracebackModule


class ServerProxy:
    def __init__(self, db_name):
        self.db_name = db_name

    def let_me_insert(self, data_set):

        collection, data = data_set
        with self.get_connection() as connection:
            id = connection[self.db_name][collection].insert_one(data)
            return id.inserted_id

    def let_me_update(self, data_set):

        collection, data, id = data_set
        with self.get_connection() as connection:
            connection[self.db_name][collection].update_one({"_id": id}, {"$set": data})

    def let_me_find_one(self, data_set):

        collection, pointer = data_set
        with self.get_connection() as connection:
            return connection[self.db_name][collection].find_one(pointer)

    def let_me_find_all(self, data_set):

        collection, pointer = data_set
        with self.get_connection() as connection:
            return connection[self.db_name][collection].find(pointer)

    def let_me_delete(self, data_set):

        collection, pointer = data_set
        with self.get_connection() as connection:
            connection[self.db_name][collection].delete_one(pointer)

    def query_field_value(self, data_set):

        collection, query, value = data_set
        with self.get_connection() as connection:
            return connection[self.db_name][collection].find({query: {"$lte": value}})

    @staticmethod
    def get_connection():
        return MongoClient(host=DbModule.host_name, port=DbModule.port)


a = ServerProxy('university')
a.query_field_value(['student', 'first_name', 'Maciejko'])