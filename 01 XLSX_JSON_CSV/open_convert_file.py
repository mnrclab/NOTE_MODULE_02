import xlrd

# untuk membuka file
file = xlrd.open_workbook('file.xlsx')
# sheet = file.sheet_by_index(0)              #untuk akses data ke sheet kerja di excel. kalau belum ada nama, jadi pake index
sheet = file.sheet_by_name('DataKaryawan')    # untuk akses data ke sheet kerja di excel based on name of sheet


# print(sheet.nrows, sheet.ncols)               #untuk mengecek jumlah kolom dan baris di index 0
# print(sheet.cell_value(0,0))                  #untuk mengecek data di cell (baris ke-0, kolom ke-0)
# print(sheet.cell_value(0,1))                  #untuk mengecek data di cell (baris ke-0, kolom ke-1)

print(sheet.nrows, sheet.ncols)
print(sheet.nrows)
print(sheet.ncols)
print(sheet.cell_value(0,1))
print(sheet.row_values(0))

for i in range(sheet.nrows):
    print(sheet.row_values(i))

# nama kolom di file xlsx
# cols = []
# for i in range(sheet.ncols):
#     print(sheet.cell_value(0, i))
# print(cols)


# print(sheet.row_values(0))                      #untuk mengambil data pada baris ke-0


# for i in range(sheet.nrows):
#     print(sheet.row_values(i))                    #akses seluruh data di file


# LATIHAN DI KELAS

# AMBIL DATA DULU DARI XLSX
data = []
for i in range(sheet.nrows):
    data.append(sheet.row_values(i)) 
print(data)

out = []
for i in data:
    out.append(dict(zip(data[0], i))) # mengubah ke dictionary
out = out[1:]
print(out)

# =========================================
# CONVERT XLSX TO CSV

# import csv
# with open('file.csv', 'w', newline='') as file:
#     kolom = list(out[0].keys())
#     tulis = csv.DictWriter(file, fieldnames=kolom)
#     tulis.writeheader()
#     tulis.writerows(out)

# =========================================
# CONVERT XLSX TO JSON

# import json
# with open('file.json', 'w') as file:
#     json.dump(out, file)

# =========================================
# MEMBUAT FILE EXCEL BARU 

import xlsxwriter

file = xlsxwriter.Workbook('test123.xlsx')
sheet = file.add_worksheet('DataKaryawan')

sheet.write(0, 0, 'Nama') #row, col, data
sheet.write(0, 1, 'Kota') #row, col, data
sheet.write(0, 2, 'Job') #row, col, data

file.close() #untuk menutup perintah sebelumnya dan menjalankan perintah membuat file baru








