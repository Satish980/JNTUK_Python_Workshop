
import csv
# empty set
cityset = set()
try:
    filename = input("Enter any filename: ")
    with open(filename,"r") as fobj:
        reader = csv.reader(fobj)
        # processing
        for line in reader:
            cityset.add(line[1])
                        ##city###
        # displaying output
        for city in cityset:
            print(city)
            
    
except FileNotFoundError as err:
    print("file doesn't exist")
except Exception as err:
    print("Unknown err :",err)