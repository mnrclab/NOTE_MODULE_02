import numpy as np

# numpy = number python
# untuk operasi matriks
# x = [1, 2, 3, 4, 5]
# y = np.array(x)

# biasa x menggunakan list [], kalau tupple tidak akan menjumlah


# print(x)
# print(y)

# print(x[::2])
# print(y[::2])

# print(x + x)
# print(y + y)

# x = [
#     [1,2,3],
#     [4,5,6] 
#     ]

# y = np.array(x)

# print(x[1][1])
# print(y[1, 1])

# numpy satu dimensi yang hanya pakai satu tanda kurung persegi [], cara cek print(x.ndim)

import numpy as np
# SATU DIMENSI
# x = [1, 2, 3]
# x = np.array(x)

# DUA DIMENSI
# y = [[1,2,3],[4,5,6]]
# y = np.array(y)

# TIGA DIMENSI
# z = [[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]]
# z = np.array(z)


# print(x)
# print(x.ndim)
# print(y)
# print(y.ndim)
# print(z)
# print(z.ndim)   #untuk menghitung berapa banyak dimensi
# print(z.size)   #untuk menghitung elemen dari matriks numpy
# print(z.dtype)  #untuk mengecek type dari matriks (int32)
# print(z.itemsize) #ukuran matriks

#MENGUBAH MENJADI FLOAT
# z = z.astype('float64')
# print(z)

# MENGHITUNG TYPE, DIMENSI, DAN SHAPE
# print(z.dtype)
# print(z.ndim)
# print(z.shape) # hasilnya 2,2,3: dimensi ke-1 ada 2 elemen, dimensi ke-2 ada 2 elemen, dimensi ke-3 ada 3 elemen

# a = np.array([1])
# print(a.ndim)
# print(a.shape)

# print(np.arange(10)) #untuk mengurutkan sebuah angka, sama dengan range, tapi tanpa koma
# print(list(range(10)))

# print(np.arange(1, 10, 2))
# print(list(range(1, 10, 2)))

# print(np.random.random(10))
# print(np.random.rand(3,4)) #memecah ke dalam 3 elemen
# print(np.random.randint(7, size=10)) #membuat dimensi sebanyak 10 element dengan angka <7
# print(np.random.randint(7, size=(2,5))) #membuat 2 dimensi masing-masing sebanyak 5 element (total 10) dengan angka <7

# SPACING
# print(np.linspace(1,10,5)) #membuat pecahan dari 1 sampai 10, dengan elemen sebanyak 5
# print(np.linspace(1,100,7)) #membuat pecahan dari 1 sampai 100, dengan elemen sebanyak 7

# a = [(1,2,3),(4,5,6),(7,8,9)]
# a = np.array(a)
# print(a[0,2]) #seperti a[0][2]
# print(a[0:, 0:2]) #tampilkan semua dimensi dengan elemen ke 1-2
# print(a[0:, 0:1]) #tampilkan semua dimensi, dengan elemen ke 1
# print(a[0:, 0]) #sama dengan sebelumnya tapi hanya menampilkan satu dimensi

#cek
# print(a[0:, 0:1].shape) #hasilnya (3,1)
# print(a[0:, 0].shape)  #hasilnya (3,) hanya hanya satu dimensi

# print(a[0:, 0:1].shape) #hasilnya (3,1)
# print(a[0:, 0:1].reshape(3,1)) 


# print(a[0:, [0,2]]) #tampilkan semua dimensi, per dimensi tampilkan elemen (index 0 DAN index 2)
# print(a[0:, [0,-1]]) #tampilkan semua dimensi, per dimensi tampilkan elemen (index 0 DAN index -1)



# ======================================================================
# a = [(1,2), (3,4)]
# print(a + a) #kalau list dikali 2
# a = np.array(a)
# print(a+ a) #mengikuti operasi matriks


# CONTOH OPERASI
# a = np.array([
#     [0,-7],
#     [-1,3]
# ])

# b = np.array([
#     [2,4],
#     [3,8]
# ])
# print(a)
# print(b)
# print(a+b)
# print(a-b)
# print(a/b)
# print(a*b)

# print(a+2) #setiap element ditambah 2

# =============================================
# x = np.array([1,2,3,4])
# print(x + x)
# print(x - x)
# print(x + 2)
# print(x - 2)
# print(x / 2)
# print(x ** 2)

# x[0] += 2 #elemen index 0 ditambah 2
# print(x)

# ==============================================
# CONTOH LATIHAN
# 2x + 1y = 5
# 1x + 1y = 7

# spldv
# | 2 1 | | x | = | 5 |
# | 1 1 | | y | = | 7 |

#penyelesaian
# a = np.array([
#     [2,1], [1,1]
# ])

# b = np.array([5,7])
# hasil = np.linalg.solve(a, b)
# print(hasil)


# SATU DIMENSI
# 3x = 6 => x = 2
# | 3 | | x | = | 6 |

# x = np.array([3]). reshape(1,1)
# y = np.array([6])
# z = np.linalg.solve(x,y)
# print(z)


# LATIHAN DI KELAS
# 4x + 7y = 2
# 3x + 2y = -5
# berapa 2x = 3y

# | 4 7 | | x | = | 2 |
# | 3 2 | | y | = | -5 |

# #penyelesaian
# a = np.array([
#     [4,7], [3,2]
# ])

# b = np.array([2,-5])
# hasil = np.linalg.solve(a, b)

# x = hasil[0]
# y = hasil[1]

# JAWABAN = (2*x) - (3*y)
# print(JAWABAN)


# LATIHAN DI KELAS
# 1a + 1k = 25
# 2a + 4k = 70

'''
| 1 1 | | a | = | 25 |
| 2 4 | | k | = | 70 |
'''

# #penyelesaian
# a = np.array([
#     [1,1], [2,4]
# ])

# b = np.array([25,70])
# hasil = np.linalg.solve(a, b)

# print(f'Jumlah ayam: {hasil[0]}, Jumlah kambing: {hasil[1]}')

# SOAL KETIGA
'''
2bt + 1p + 1h = 4700
1bt + 2p + 1h = 4300
3bt + 2p + 1h = 7100

| 2 1 1 | | bt | = | 4700 |
| 1 2 1 | | p | = | 4300 |
| 3 2 1 | | h | = | 7100 |
'''
# #penyelesaian
# a = np.array([[2,1,1], [1,2,1], [3,2,1]])
# b = np.array([4700,4300,7100])
# hasil = np.linalg.solve(a, b)

# print(f'harga buku tulis: Rp {round(hasil[0])}, harga pencil: Rp {round(hasil[1])}, harga penghapus: Rp {round(hasil[2])}')


#======================================
# x = [1,2,3,4,5]
# y = np.array(x)

# print(max(x))
# print(max(y))

# print(y.max())
# print(y.min())


# MEMBUAT FUNCTION SENDIRI
# def maks(a):
#     a.sort()
#     return a[-1]

# def mins(a):
#     a.sort()
#     return a[0]

# from functools import reduce
# def sums(a):
#     return reduce(lambda a,b: a+b, a)

# z = [1,2,3,4,5,6,7]
# print(maks(z))
# print(min(z))
# print(sums(z))

# DARI MAS LINTANG
# from functools import reduce
# z = [1,2,3,4,5,6,7]
# zsum = reduce(lambda a,b: a+b, z)
# zmax = reduce(lambda a,b: a if (a>b) else b, z)
# zmin = reduce(lambda a,b: a if (a<b) else b, z)

# #==================
# y = np.array(z)
# print(np.mean(y))
# print(np.median(y))
# print(np.pi)
# print(np.sin(0))
# print(np.cos(0))

# z = [[1,2,3,4,5], [1,20,400,300,2]]
# y = np.array(z)
# print(y)
# print(y.max())
# print(y.min())
# print(np.argmax(y)) #memberitahu index dalam list
# print(np.argmin(y)) #memberitahu index dalam list

# cek dimensi
z = [[1,2,3,4,5], [1,20,400,300,2]]
y = np.array(z)
# print(y.shape) # 2,5
# print(y.reshape(10)) #menjadi satu dimensi dengan elemen 10
# print(y.reshape(-1)) #menjadi satu dimensi dengan elemen terserah
# print(y.reshape(5,2))
# print(y.reshape(-1, 1, 2))