import csv
# empty set
citylist = list()
try:
    filename = input("Enter any filename: ")
    with open(filename,"r") as fobj:
        reader = csv.reader(fobj)
        # processing
        for line in reader:
            if line[1] not in citylist:
                citylist.append(line[1])
                        ##city###
        # displaying output
        for city in citylist:
            print(city)
            
    
except FileNotFoundError as err:
    print("file doesn't exist")
except Exception as err:
    print("Unknown err :",err)