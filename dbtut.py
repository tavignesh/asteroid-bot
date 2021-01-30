import pymongo
import string
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://bot:1234@cluster0.5bkqm.mongodb.net/discord?retryWrites=true&w=majority")
db = cluster["discord"]
collection = db["bot"]

post = {"_id": 23, "namehere": "op man", "haha": "pye", "num": 4}
# collection.insert(post)
# fio = collection.update_one({"_id":780625655657791518},{"$set":{"badwords":["uluak","@34",5434]}})
# for i in fio:
# print(fio)
a = list(string.ascii_letters)
df = "Kglsdo dfaD"
print(string.capwords(df))
print(a)