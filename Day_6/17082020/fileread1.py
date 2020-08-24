
#### reading line by line
# fobj acts as cursor|pointer|reference
with open("numbers.txt","r") as fobj:
    for line in fobj:
        line = line.strip()   # remove white spaces if any
        output = line.split(":")
        print("Record no :",output[0])
        print("Language  :", output[1])
        print("------------------")
        
        
#### using read()
with open("numbers.txt","r") as fobj:
    ## reading the complete file to the SINGLE string 
    print(fobj.read())     
    

## readlines(): Each line will be complete to the string 
## read lines() will return the list
with open("numbers.txt","r") as fobj:
    ## reading the complete file to the SINGLE string 
    print(fobj.readlines())     
    
    
### using csv library
## Advantage : each line will be converted to the list automatically
import csv
#step1 : open the file
with open("numbers.log","r") as fobj:
    # converting file object  -----> csv object
    reader = csv.reader(fobj,delimiter='|')
    for line in reader:
        print(line)



import csv
#step1 : open the file

try:
    filename = input("Enter any filename :")
    with open(filename,"r") as fobj:
    
        reader = csv.reader(fobj,delimiter='|')
        for line in reader:
            print(line)
except FileNotFoundError as err:
    print("file doesn't exist")
except TypeError as err:
    print("INvalid operation")
except KeyError as err:
    print("Dictionary key doesn't exist")
except Exception as error:
    print("System defined error :", error)
    print("Unknown error")
finally:
    print("ENf of the file handling")
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
     