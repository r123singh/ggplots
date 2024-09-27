import pandas as pd
import numpy as np
from pandas import DataFrame, Series
from io import StringIO

data = """Date, Pollster, State, Party,Est
13/03/2014, Newspoll, NSW, red, 25
13/03/2014, Newspoll, NSW, blue, 28
13/03/2014, Newspoll, Vic, blue, 24
13/03/2014, Newspoll, Vic, red, 23
13/03/2014, Galaxy, NSW, red, 23
13/03/2014, Galaxy, NSW,blue, 24
13/03/2014, Galaxy, Vic, red, 26
13/03/2014, Galaxy, Vic, blue, 25"""

df = pd.read_csv(StringIO(data), header=0,skipinitialspace= True)

print(df)

print("-------------------------------------------------------")
#pivot to wide format on party column
#setup multiindex for other columns

df1 = df.set_index(['Date','Pollster','State'])
#2: do the pivot
wide1 = df1.pivot(columns='Party')
print(wide1)
