import pandas as pd
from pandas import DataFrame, Series
import numpy as np

dti = pd.DatetimeIndex(pd.date_range(start = '5/1/2011', periods = 12, freq = 'ME'))
s = Series([1,2,3,4,5,6,7,8,9,10,11,12], index=dti )
print(s)

na = dti.to_pydatetime() #numpy array
print(na)

