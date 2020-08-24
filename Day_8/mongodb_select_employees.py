import pymongo
import json
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["jntu_univ"]
mycol = mydb["staff"]


for x in mycol.find():
  #street = x['street']
  #print(street)
  print(x)