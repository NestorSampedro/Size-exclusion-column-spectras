#Read, parse and plot ctv sheets from AKTA  GO
#Python modules necessary: Pandas and matplotlib
#Parameters to change: name of file to parse, ax.set_title and range for differnet volumes.

import pandas as pd

pd.options.display.max_rows = 9999
df = pd.read_csv('NS 210323 PXT-2F  001.csv', encoding="utf16", sep ='\t', skiprows=2)

mAU=[]
ML=[]

# filter data based on the first column
#mAU = df.loc[(df.iloc[:, 0] >= 10.0) & (df.iloc[:, 0] <= 26.0), 'mAU'].values
#ML = df.loc[(df.iloc[:, 0] >= 10.0) & (df.iloc[:, 0] <= 26.0), 'ml'].values

#Pick every 20th value between 10 and 28 mL
mAU = df.loc[(df.iloc[:, 0] >= 8.0) & (df.iloc[:, 0] <= 28.0) & (df.index % 20 == 0), 'mAU'].values
ML = df.loc[(df.iloc[:, 0] >= 8.0) & (df.iloc[:, 0] <= 28.0) & (df.index % 20 == 0), 'ml'].values


import matplotlib.pyplot as plt
import numpy as np

# plot the data
plt.figure(figsize=(5,5))  #Change the size of the graph
ax=plt.subplot()
#ax.set_title('NA6 NAR MST triplicates fitting KD', fontsize=20) #Title and size
ax.set_xlabel('mL', fontsize=20) #X legend and size
ax.set_ylabel('mAU', fontsize=20) #Y legend and size
ax.set_title('210323 PXT', fontsize=24)  # Add a title to the axes.
#plt.xscale("log")
#plt.ylim(878.5,897.5)
plt.plot(ML,mAU)
ax.set_facecolor('1') #background color
plt.xticks(fontsize=20) #x ticks and size
ax.set_xticks(range(8, 30, 2))
plt.yticks(fontsize=20) #y ticks and size
plt.show()
