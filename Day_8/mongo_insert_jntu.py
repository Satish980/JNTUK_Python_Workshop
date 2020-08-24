import pymongo
import json
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["jntuk"]
mycol = mydb["staff"]

# reading the file
with open('realestate_csv.json')  as f:
    # returns JSON object as  
    # a dictionary 
    data = json.load(f) 


### inserting all the records
x = mycol.insert_many(data)

#print list of the _id values of the inserted documents:
#print(x.inserted_ids)

## select query ( displaying all the records)
for x in mycol.find():
    print(x)
    print("--------------")
