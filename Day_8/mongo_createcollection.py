import pymongo

# establishing your connection
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]    # creating your database

mycol = mydb["customers"]        #creating table

print(mydb.list_collection_names())