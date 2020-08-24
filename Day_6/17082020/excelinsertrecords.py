import csv
from openpyxl import Workbook
wb = Workbook()

# grab the active worksheet  # creating one sheet
ws = wb.active

# requirement : reading csv file and inserting to excel

with open("realestate.csv","r") as fobj:
    ## converting file object to csv object
    reader = csv.reader(fobj)
    for line in reader:
        #print(line)
        ws.append(line)



# Save the file
wb.save("realestate_info.xlsx")