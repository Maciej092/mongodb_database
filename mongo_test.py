import pymongo
from pymongo import MongoClient

cluster = pymongo.MongoClient("mongodb+srv://testUser:kajamaria%4020170814@cluster0-cywqs.mongodb.net/test?retryWrites=true&w=majority")
db = cluster.test
db = cluster["test"]
collection = db["test"]

post = {
    "_id": 0,
    "name": 'maciej'
}
collection.insert_one(post)