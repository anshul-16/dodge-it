'''from xlrd import open_workbook

book = open_workbook("trial sheet.xlsx")
sheet = book.sheet_by_index(0)

column1 = []
column2 = []

for row in range(0,10): #start from 1, to leave out row 0
    column1.append(sheet.cell(row, 0)) #extract from first col

print(column1)

for i in range(10):
    column2.append()

print(column2[0])'''

import csv

#your_list = []

with open('trial sheet.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)

print your_list
print (your_list[0][0])