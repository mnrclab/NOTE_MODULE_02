import numpy as np

# Membuat vertical
# x = np.loadtxt('0.csv', 
# skiprows=1, delimiter=',',
# )
# print(x)


# Membuat horizontal
# x = np.loadtxt('0.csv', 
# skiprows=1, delimiter=',',
# unpack=True
# )
# print(x)


# MENGAMBIL DATA SECARA TERPISAH
# a, b= 12, 13
# print(a)
# print(b)

id, usia = np.loadtxt('0.csv', 
skiprows=1, delimiter=',',
unpack=True
)

# print(id)
# print(usia)

# cara pertama 
np.savetxt('1.csv', (np.c_[id, usia]), fmt='%d',
    header='id, usia', comments='', delimiter=','
    )

# cara alternatif 2
# data = np.array(list(map(lambda  a,b: [a,b], id, usia)))
# np.savetxt('1.csv', data, fmt='%d',
#     header='id, usia', comments='', delimiter=','
#     )