import xlrd

xlsfile = 'loupanzidian.xls'
book = xlrd.open_workbook(xlsfile)
sheet_name = book.sheet_names()
print(sheet_name)
sheet = book.sheet_by_index(0)
nrows = sheet.nrows
ncols = sheet.ncols
print(nrows)
print(ncols)
list = []
for i in range(0, nrows):
    value = sheet.cell(i, 0)
    list.append(value)

list = list.__str__().replace("text:", "").replace("'", "").replace("]", "").replace("[", "").replace(",", "").split()
list = sorted(list, key=lambda x: len(x))
print(list)
