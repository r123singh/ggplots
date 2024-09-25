import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

plt.style.use('ggplot')

a = np.random.normal(0,1,999)
b= np.random.normal(1,2,999)
c = np.random.normal(2,3,999)
df = pd.DataFrame([a,b,c]).T
df.columns = ['A', 'B', 'C']

df1= df.cumsum()
ax = df1.plot()

#standard plot output
ax.set_title('Title')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')

fig = ax.figure
fig.set_size_inches(8,3)
fig.tight_layout(pad=1)
fig.savefig('lineplot.png', dpi=125)

plt.close()

#box plot output
ax = df.plot.box(vert=False)
ax.set_title('Title')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')

fig = ax.figure
fig.set_size_inches(8,3)
fig.tight_layout(pad=1)
fig.savefig('boxploat.png', dpi = 125)

plt.close()

# standard histogram plot output

ax =  df['A'].plot.hist(bins=20)

ax.set_title('Title')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')

fig = ax.figure
fig.set_size_inches(8,3)
fig.tight_layout(pad=1)
fig.savefig('histogram.png', dpi=125)

plt.close()



