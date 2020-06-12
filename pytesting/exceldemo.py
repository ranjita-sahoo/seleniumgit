import openpyxl

book = openpyxl.load_workbook("C:\\Users\\Sudhir\\Desktop\\Book1.xlsx")
sheet = book.active
cell = sheet.cell(row=4, column=3)
print(cell.value)