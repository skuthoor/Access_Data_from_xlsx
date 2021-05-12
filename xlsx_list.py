import xlrd

path = "List_of_Blood_Centers_in_Kerala.xlsx" #List_of_Blood_Centers_in_Kerala

book = xlrd.open_workbook(path)
sheet = book.sheet_by_index(0)

name = []
address= []
district = []
govt_pvt = []
category = []

print(sheet.cell_value(3,1))
print(sheet.nrows)

for i in range(2,sheet.nrows):
	name.append(str(sheet.cell_value(i,1)))
	address.append(str(sheet.cell_value(i,2)))
	district.append(str(sheet.cell_value(i,3)))
	govt_pvt.append(str(sheet.cell_value(i,4)))
	category.append(str(sheet.cell_value(i,5)))

#print(name)

