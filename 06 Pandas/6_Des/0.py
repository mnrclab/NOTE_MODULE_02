#HANDLING NaN Value

#USING REPLACE

import pandas as pd
import numpy as np 


df = pd.read_csv('data.csv')

# df = df.replace('-', 0)
# df = df.replace(['-','#'], 0)

# MENGUBAH 2 KONDISI
# df = df.replace(['-','#'], np.NaN)
# df = df.fillna('XXX')

# MENGUBAH 2 KONDISI
# df = df.replace({
#     '-': '+',
#     '#': np.NaN
# })

# MENGUBAH DI KOLOM TERTENTU
# df = df.replace({
#     'usia': ['-','#']
# }, np.NaN)

# print(df)

# MENGUBAH DI 2 KOLOM 
# df = df.replace({
#     'usia': ['-','#'],
#     'nama': '#'
# }, np.NaN)

# print(df)


# MENGUBAH DI 2 KOLOM 
# df = df.replace({
#     'usia': ['-','#','0'],
#     'nama': '#'
# }, {
#     'usia': np.NaN,
#     'nama':'Anonim'
#     })

# print(df)

# MENGISI DATA KOSONG DENGAN FORWARD FILLING
df['usia'] = df['usia'].replace(
    to_replace= '-',
    method= 'ffill'
)
print(df)