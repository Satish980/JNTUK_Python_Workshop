
from openpyxl import Workbook
wb = Workbook()

# grab the active worksheet  # creating one sheet
ws = wb.active



# Rows can also be appended

for val in range(1,100):
    ws.append([val])


# Save the file
wb.save("sample_numbers.xlsx")