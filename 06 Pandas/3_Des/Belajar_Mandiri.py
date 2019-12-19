import pandas as pd 
import numpy as np 

# MISSING DATA

df = pd.DataFrame(
    {'A':[1,2,np.nan],
    'B':[5,np.nan,np.nan],
    'C':[1,2,3]
    }
)
# print(df)

#Dropna() Method
#Menghapus atau eliminasi data yang kosong
x = df.dropna()
# print(x)

y = df.dropna(axis=1)
# print(y)

z = df.dropna(thresh=2) #menampilkan 1 yang kosong
# print(z)

r = df.dropna(thresh=1) #menampilkan 2 yang kosong
# print(r)

# MENGISI BAGIAN KOSONG
w = df.fillna(value='lupa input')
# print(w)

e = df['A'].fillna(value=df['A'].mean())
print(e)