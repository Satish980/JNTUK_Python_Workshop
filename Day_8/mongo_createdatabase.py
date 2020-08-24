import pymongo

#In MongoDB, a database is not created until it gets content
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]   # creating your database



