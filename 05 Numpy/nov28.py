import numpy as np 

# a = np.array([[1,2,3], [4,5,6]])
# b = np.array([[0,0,0], [0,0,0]]) #matriks identitas
# print(b.dtype)
# c = np.zeros((2,3), dtype='int32') #membuat matriks zero (0) dg type disamakan int32
# print(c.dtype)
# print(c)

# d = np.array([[1,2,3], [1,2,3], [1,2,3]])
# e = np.ones((3,3))
# print(d*e)

# =======================================

# x = np.zeros((3,3), dtype=bool)
# print(x)

# x = np.ones((3,3), dtype=bool)
# print(x)

# lain = np.full((3,3), 1, dtype=bool) #membuat matriks dengan isi penuh dengan angka 1, dan diubah dalam type: boolean
# print(lain)

# lain = np.full((3,3), 1)
# print(lain)
# print(type(lain))
# lainlist = lain.tolist() #mengubah numpy.ndarray menjadi list
# print(lainlist)
# print(type(lainlist))

# ============================================
import numpy as np 
# x = [1, 2, 3, 4, 5]
# y = [6, 7, 8, 9, 10]
# # gimana supaya z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # cara 1
# z = []
# z.append(x)
# z.append(y)
# print(z)

# # cara 2
# z = [x, y]
# print(z)

# # cara 3
# z = np.array(x+y).reshape(2,-1).tolist()
# print(z)

# # cara 4
# a = []
# a.extend(x)
# a.extend(y)
# z = np.array(a).reshape(2, -1).tolist()
# print(z)

# # cara 5
# xnp = np.array(x)
# ynp = np.array(y)
# z = np.concatenate([[xnp],[ynp]], axis=0).tolist()
# print(z)

# # cara 6
# z = np.vstack([xnp, ynp]).tolist()
# print(z)

# # cara 7
# z = np.r_[[xnp], [ynp]].tolist()
# print(z)

# # cara 8
# z = np.row_stack((xnp, ynp)).tolist()
# print(z)



# ===================================================

# a = np.arange(6).reshape(2, -1)
# b = np.array([5,6,7,8,9,10]).reshape(2, -1)

# c = np.vstack([a,b])
# d = np.concatenate([a,b], axis=0)
# e = np.row_stack((a,b))
# f = np.r_[a,b]
# print(c)
# print(d)
# print(c)
# print(c)


# z = np.arange(1, 11)
# print(z)
# print(z[1::2])
# print(z[z % 2 == 0])
# print(z[z % 2 != 0])
# z[z%2 != 0] = 0
# print(z)

# z = np.arange(1, 11)
# print(np.where(z%2 != 0, 0, z)) #jika elemen z ..condition... ubah menjadi 0

# x = np.arange(10, 20) #menampilkan 10....19
# # print(np.where(x<6))
# # print(x[np.where(x<16)])
# print(x[np.where((x<16) & (x<18))])
# print(x[np.where(np.logical_and(x<14, x<18))])
# print(x[(x>14) & (x>18)])





# ==================================================================
# DETERMINAN
# x = np.array([[3,1], [2,5]]) # (3x5)-(1x2)
# print(np.linalg.det(x))

# y = np.array([[1,2,1],[3,3,1],[2,1,2]])
# print(y)
# print(np.linalg.det(y))


# INVERS
z = np.array([[3,2], [1,4]])
print(z)
print(np.linalg.inv(z))

# DOT PRODUCT
print(z@np.linalg.inv(z))
print(z.dot(np.linalg.inv(z)))

# CROSS PRODUCT
print(np.cross(z,z))
