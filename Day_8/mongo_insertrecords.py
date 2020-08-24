import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]   # creating your database
mycol = mydb["customers"]       # creating tablename

mydict = { "name": "Giri", "address": "Machilipatnam" }
## inserting record
x = mycol.insert_one(mydict)
print(x.inserted_id)

mydict = { "name": "Kiran", "address": "Hyderabad" }
# inserting another record
x = mycol.insert_one(mydict)

print(x.inserted_id)

print(mydb.list_collection_names())