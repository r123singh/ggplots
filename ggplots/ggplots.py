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

#multiple histograms overlapping
ax = df.plot.hist(bins = 25, alpha = 0.5)

ax.set_title('Title')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')

fig = ax.figure
fig.set_size_inches(8,3)
fig.tight_layout(pad = 1)
fig.savefig('overlap-histogram.png', dpi =125)

plt.close()

# multiple histogram stacked

ax = df.plot.hist(bins = 25, stacked = True)

ax.set_title('Title')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')

fig = ax.figure
fig.set_size_inches(8,3)
fig.tight_layout(pad=1)
fig.savefig('stacked-histogram.png', dpi = 125)

plt.close()


#plotting bar chart output

bins = np.linspace(-10,15.26)
binned = pd.DataFrame()
for x in  df.columns:
	y = pd.cut(df[x], bins, labels = bins[:-1])
	y = y.value_counts().sort_index()
	binned = pd.concat([binned, y],axis =1)
binned.index =  binned.index.astype(float)
binned.index+= (np.diff(bins)/2.0)
ax = binned.plot.bar(stacked = False, width = 0.8)

ax.set_title('Title')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')

fig = ax.figure
fig.set_size_inches(8,3)
fig.tight_layout(pad=1)
fig.savefig('bar-chart.png', dpi=125)

plt.close()

