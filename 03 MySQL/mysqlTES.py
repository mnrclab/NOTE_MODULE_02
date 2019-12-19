# py -m pip install MySQL-connector-python

import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'kahfi2008',
    database = 'ptabc'
)

#UNTUK MENAMPILKAN DATA SAJA
# c = db.cursor()
# c = db.cursor(dictionary=True) #mengubah database dalam bentuk dictionary
# query = 'select * from karyawan' #query atau perintah untuk menjalankan mysql
# c.execute(query)
# out = c.fetchall()
# print(out)
# print(list(map(lambda x: x[0], out)))

#UNTUK MENAMBAHKAN DATA
# c = db.cursor(dictionary=True) #mengubah database dalam bentuk dictionary
# query = 'insert into karyawan (nama) values (%s)' #query atau perintah untuk menjalankan mysql
# data = ('Andi',) #memasukkan data Andi
# c.execute(query, data)
# db.commit()

# c = db.cursor()
# sql = 'insert into karyawan (nama, gaji) values (%s, %s)'
# val = ('Andi', 15000000)
# c.execute(sql, val)
# db.commit()
# print(c.rowcount, 'Data tersimpan')

# c = db.cursor()
# sql = 'insert into karyawan (nama, gaji) values (%s, %s)'
# val = [('Cici', 15000000), ('Caca', 15000000)]
# c.executemany(sql, val)
# db.commit()
# print(c.rowcount, 'Data tersimpan')

#UNTUK MENGHAPUS DATA
# c = db.cursor(dictionary=True) 
# query = 'delete from karyawan where nama = (%s)' #query atau perintah untuk menjalankan mysql
# data = ('Andi',)
# c.execute(query, data)
# db.commit() #PERINTAH UNTUK TAMBAH, HAPUS, DAN UPDATE DATA

#UNTUK MENGUPDATE DATA
# c = db.cursor(dictionary=True) 
# query = 'update karyawan set nama = %s where nama = %s' #query atau perintah untuk menjalankan mysql
# data = ('Hani', 'Ani',)
# c.execute(query, data)
# db.commit() #PERINTAH UNTUK TAMBAH, HAPUS, DAN UPDATE DATA

#MENGUBAH ISI DATA BEBERAPA DATA SEKALIGUS
# c = db.cursor(dictionary=True) 
# query = 'update karyawan set nama=%s, gaji=%s where id_kar=%s '
# data = ('Zizi', 20000000, 9)
# c.execute(query, data)
# db.commit() 

#MENAMBAH COLUMN 'HOBBY'
c = db.cursor(dictionary=True) 
query = 'alter table karyawan add column hobby varchar(255) '
c.execute(query)
db.commit()


#BAHAN BELAJAR
# https://www.codeproject.com/Articles/33052/Visual-Representation-of-SQL-Joins

'''LATIHAN
web scrapping digimon dan disimpan ke database
https://github.com/LintangWisesa/Ujian_AnalyticsVisualization_JCDS05
https://www.stat.fi/index_en.html
'''