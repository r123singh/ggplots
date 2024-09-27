import numpy as np
import pandas as pd
from pandas import DataFrame, Series

#missing data in series

s = Series([8, None, float('nan'), np.nan])
print(s)
n = s.isnull()
print(n)

p = s.notnull()
print(p)

c = s.fillna(0)
print(c)

#missing data in dataframe
data = {1:[1,2,np.nan], 2:[1,9,np.nan], 3: [np.nan,np.nan,np.nan]}
df = DataFrame(data)

print(df)

df1 = df.dropna()
print(df1)

df2 = df.dropna(axis=1)
print(df2)

df3 = df.dropna(how='all')
print(df3)

df4 = df.dropna(thresh=2)
print(df4)


