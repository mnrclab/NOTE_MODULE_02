import pymongo
import datetime
dburl = 'mongodb://localhost:27017/'
mymongo = pymongo.MongoClient(dburl)

# MELIHAT DAFTAR DATABASE
# dbs = mymongo.list_database_names()
# print(dbs)

# MENGAKSES COLLECTION DALAM DATABASE 'pymongodb'
# mydb = mymongo['pymongodb']
# mycol = mydb['colmong']
# alldata = list(mycol.find())
# print(alldata)

# MENGAKSES DATA KHUSUS DENGAN NAMA 'Andi'
# alldata = list(mycol.find({'nama':'Andi'}))
# print(alldata)

# MENGAKSES HANYA HANYA NAMA DENGAN NAMA 'Andi'
# alldata = list(mycol.find({'nama':'Andi'}, {'nama':1}))
# print(alldata)

# MENGAKSES DATA YANG HANYA BERUSIA > 24
# alldata = list(mycol.find({'usia': {'$gt': 24}}))
# print(alldata)

# MEMASUKKAN SATU DATA
# mydata = {'nama': 'Deni', 'usia':18, 'kota': 'Kediri'}
# mycol.insert_one(mydata)

# MEMASUKKAN BEBERAPA DATA
# mydata = [
#     {'nama': 'Euis', 'usia':35, 'kota': 'Denpasar'},
#     {'nama': 'Fafa', 'usia':29, 'kota': 'Jakarta'},
#     {'nama': 'Gian', 'usia':22, 'kota': 'Sorong'}
# ]
# x = mycol.insert_many(mydata)
# print(x.inserted_ids) #untuk nambah data sekaligus cek object id yang telah terinput

# x = mycol.insert_one({'nama':'Nino'})
# print(x.inserted_id) #kalau cuma satu data
# print(list(mycol.find({'_id': x.inserted_id})))

# MENCARI BEBERAPA DATA
# nama = ['Andi', 'Euis', 'Fafa']
# x = list(mycol.find({'nama': {'$in': nama}}))
# print(x)

# MENGHAPUS SATU DATA 'Fafa'
# x = {'nama': 'Fafa'}
# mycol.delete_one(x)

# MENGHAPUS SELURUH DATA 'Gian'
# x = {'nama': 'Gian'}
# mycol.delete_many(x)

# MENGHAPUS SELURUH DATA
# mycol.delete_many({})


# MENGUPDATE DATA
# data = {'nama':'Euis'}
# new = {'nama': 'Gus De'}
# mycol.update_one(data, {'$set': new})

# UPDATE yang usia > 25 & usia < 30, update nama = 'Youngman'
# data = {'$and': [
#     {'usia': {'$gt': 25}},
#     {'usia': {'$lt': 30}},
# ]}

# new = {'nama': 'Youngman'}
# mycol.update_many(data, {'$set': new})



# =========================================================================
mydb = mymongo['hahaha']
mycol = mydb['hahaha1']

# mycol.insert_one({
#     'nama':'Budi', 'waktu': datetime.datetime.now() 
# })
# print(list(mycol.find()))
# query = mycol.find({'nama':'Budi'}, {'waktu':1})
# print(list(query)[0]['waktu'])


import pytz
jkt = pytz.timezone('Asia/jakarta')
mycol.insert_one({
    'nama':'Deni', 'waktu': datetime.datetime.utcnow() #untuk mengacu pada jam dunia, London, => Indonesia + 7
})

query = mycol.find({'nama':'Deni'}, {'waktu':1})
print(jkt.localize(list(query)[0]['waktu']))