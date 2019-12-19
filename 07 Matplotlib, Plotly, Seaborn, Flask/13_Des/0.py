import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as im
import mpl_toolkits.mplot3d.axes3d

# df = pd.read_csv('dataSales.csv')
# df = df.pivot(index='nama', columns='mobil')

# fig, p = plt.subplots()
# plt.imshow(df, cmap='BuPu_r') #MEMBALIK DATANYA
# plt.colorbar()

# col = list(map(lambda x: x[1], df.columns.tolist()))
# i = list(map(lambda x: x, df.index.tolist()))

# for x in range(len(i)):
#     for y in range(len(col)):
#         p.text(y, x, df.iloc[x, y],
#                        ha="center", va="center", color="k")

# p.set_xticks(np.arange(len(col)))
# p.set_xticklabels(col)

# p.set_yticks(np.arange(len(i)))
# p.set_yticklabels(i)

# plt.show()


# 3DPLOT
# fig = plt.figure()
# p = plt.subplot(111, projection='3d')
# data = range(11)
# x = np.array(data)

# p.plot_wireframe(
#     x, x, x.reshape(1,-1), color='r', linestyle=':'
#     )

# p.scatter(x,x,x, marker='o', color='y', s=150)
# p.set_xlabel('Sumbu X')
# p.set_ylabel('Sumbu Y')
# p.set_zlabel('Sumbu Z')

# plt.show()


# 3D PLOT

fig = plt.figure('Tes 3D')
p = plt.subplot(111, projection='3d')

x = np.arange(10) #data x 
y = np.ones(10) #data y
z = np.zeros(10) #titik mulainya bar

dx = np.ones(10)
dy = np.ones(10)
dz = np.arange(10) #data z

p.bar3d(x, y, z, dx,dy,dz)
p.set_xlabel('Sumbu X')
p.set_ylabel('Sumbu Y')
p.set_zlabel('Sumbu Z')
plt.show()