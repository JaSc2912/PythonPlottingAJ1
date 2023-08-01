

import pandas as pd

import matplotlib.pyplot as plt

 

headers = ['date', 'value']

 

df = pd.read_csv("/dataexport_20230626T064417.csv", names=headers)

 

d = df['date']

v = df['value']

 

plt.plot(d, v)

plt.show()