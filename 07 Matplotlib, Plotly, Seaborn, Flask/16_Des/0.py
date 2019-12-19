import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as im
import mpl_toolkits.mplot3d.axes3d

df = pd.read_excel(
    'indo.xlsx',
    index_col='Unnamed: 0',
    na_values=['-'],
    header = 3,
    skipfooter = 3
)
df = df.fillna(0)

plt.style.use('seaborn')

fig = plt.figure('Tes 3D', figsize=(15,8))
p = plt.subplot(111, projection='3d')

x = np.arange(len(df.index))
y = np.arange(len(df.index)) #data y
z = np.zeros(len(df.index)) #titik mulainya bar

dx = np.ones(len(df.index))
dy = np.ones(len(df.index))
dz = df[2010] #data z

p.bar3d(x, y, z, dx,dy,dz)
p.set_ylabel('Tahun 2010')
p.set_zlabel('Popolasi 2010')
p.set_xticks(np.arange(len(df.index)))
p.set_xticklabels(df.index, rotation=90)
plt.show()