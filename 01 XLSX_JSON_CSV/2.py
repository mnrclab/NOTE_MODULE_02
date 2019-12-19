import xlsxwriter

file = xlsxwriter.Workbook('z.xlsx')    #membuat file baru
sheet = file.add_worksheet('Data')

sheet.write(0,0,1)                      #menambah data '1' di row 0 col 0
sheet.write(0,1,'=2*2')                 #menambah fungsi perkalian di row 0 col 1
sheet.write(0,2,'=A2 + 200')            #menambah nilai 200 di kolom A2
sheet.write(0,2, '=SUM(A1:B1)')         #melakukan operasi SUM 

for i in range(10):
    sheet.write(i, 0, i)
file.close()

import xlrd
file = xlrd.open_workbook('z.xlsx')
sheet = file.sheet_by_name('Data')
for i in range(sheet.nrows):
    print(sheet.cell_value(i, 0))


# SUMBER DATA: CSV, JSON, XLSX, API, SQL


# API = APLICATION PROGRAMMING INTERFACE
# REST API YANG AKAN DIPELAJARI