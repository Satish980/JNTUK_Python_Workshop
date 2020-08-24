
import json 

# Opening JSON file 
with open('realestate_csv.json')  as f:
    # returns JSON object as  
    # a dictionary 
    #converting file object to dictionary
    data = json.load(f) 
      
    # Iterating through the json 
    # list
    fobj = open("tocsv.csv","w")
    for i in data: 
        print(i) 
        print("------------")
        street = i['street']
        city = i['city']
        record = ",".join([street,city])
        fobj.write(record + "\n")
        
        
      
