# import xlrd
# file = xlrd.open_workbook('file.xlsx')
# sheet = file.sheet_by_name('DataKaryawan')

# data = []
# for i in range(sheet.nrows):
#     data.append(sheet.row_values(i)) 
# print(data)


# LATIHAN DI KELAS
# MEMBUAT FILE XLSX BARU DARI DATA FILE LAMA XLSX

# CARA SENDIRI
# header = data[0]
# value = data[1:]

# import xlsxwriter
# file_baru = xlsxwriter.Workbook('test1234.xlsx')
# sheet = file_baru.add_worksheet('DataKaryawan')

# for i in range(len(value)+1):
#     for j in range(len(header)):
#         sheet.write(i, j, data[i][j])

# file_baru.close()


# CARA DARI PENGAJAR
# col = ['no', 'nama', 'kota']
# data = [
#     [1, 'Andi', 'Jakarta'],
#     [2, 'Budi', 'Surabaya'],
#     [3, 'Caca', 'Bandung']
# ]

# import xlsxwriter
# filebaru = xlsxwriter.Workbook('test12345.xlsx')
# sheet = filebaru.add_worksheet('DataSiswa')

# #write col
# for i in col:
#     sheet.write(0, col.index(i), i)

# #write data
# row = 1
# for x, y, z in data:
#     sheet.write(row, 0, x)
#     sheet.write(row, 1, y)
#     sheet.write(row, 2, z)
#     row += 1

# filebaru.close()

# MENGUBAH FILE JSON KE DALAM XLSX
# import json
# with open('file.json', 'r') as file:
#     x = json.load(file)

# col = list(x[0].keys())
# data = []
# for i in x:
#     data.append(list(i.values()))

# import xlsxwriter
# file = xlsxwriter.Workbook('dataExt.xlsx')
# sheet = file.add_worksheet('SheetA')

# #write col
# for i in col:
#     sheet.write(0, col.index(i), i)

# #write data
# row = 1
# for x, y, z, q in data:
#     sheet.write(row, 0, x)
#     sheet.write(row, 1, y)
#     sheet.write(row, 2, z)
#     sheet.write(row, 3, q)
#     row += 1

# file.close()



# otomatisasi kolom nomor