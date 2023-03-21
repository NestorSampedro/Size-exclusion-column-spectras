#Read, parse and plot ctv sheets from AKTA  GO
#Python modules necessary: Pandas and matplotlib
#Parameters to change: name of file to parse, ax.set_titles for the differennt samples

import pandas as pd
import matplotlib.pyplot as plt

# Parameters to change
filename1 = 'NS 210323 PXT-2F KCL 001.csv'
filename2 = 'NS 210323 PXT-2F  001.csv'
title = '210323 PXT-2F'

# Read and parse the data from both csv files
dfs = []
for filename in [filename1, filename2]:
    df = pd.read_csv(filename, encoding="utf16", sep='\t', skiprows=2)
    mAU = df.loc[(df.iloc[:, 0] >= 8.0) & (df.iloc[:, 0] <= 28.0) & (df.index % 20 == 0), 'mAU'].values
    ML = df.loc[(df.iloc[:, 0] >= 8.0) & (df.iloc[:, 0] <= 28.0) & (df.index % 20 == 0), 'ml'].values
    dfs.append((ML, mAU))

# Create a subplot and plot the data from both data frames onto it
fig, ax = plt.subplots(figsize=(8, 6))
colors = ['red', 'blue']
labels = ['PXT2F TX+KCL', 'PXT2F TX']
for i in range(len(dfs)):
    ax.plot(dfs[i][0], dfs[i][1], color=colors[i], label=labels[i])

# Customize the plot as desired
ax.set_xlabel('mL', fontsize=16)
ax.set_ylabel('mAU', fontsize=16)
ax.set_title(title, fontsize=20)
ax.set_facecolor('1')
ax.tick_params(axis='both', which='major', labelsize=14)
ax.set_xticks(range(8, 30, 2))
ax.legend(fontsize=14)
plt.show()
