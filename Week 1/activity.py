#Amanda Holbrook
#CS 4900
#Pattern Discovery in 3D Genome Data
#Assignment #1
#OBTAINING AND EXPLORING GAM DATA


import pandas as pd
import numpy as np

out = open('results.csv', 'w')

#getting data file into dataframe
infile = input("\n\nInput testing file: ")
print("\n\nReading file...")
data = pd.read_csv(infile, sep='\t', index_col=0)
# num windows = num col
windows = data.index.size
# num nps = num rows
nps = len(list(data)) - 2

#a dataframe without start/stop columns
nowindows = data.drop(["start"], axis=1)
nowindows = nowindows.drop(["stop"], axis=1)


print("Calculating Stats for NPs...")

#added col for total nps
data['Total_NPs'] = nowindows.sum(axis = 1)
nowindows['Total_NPs'] = nowindows.sum(axis = 1)

# data.to_csv(out)
# nowindows.to_csv(out2)

#get max min mean of nps
maxnp = nowindows['Total_NPs'].max(skipna=True)
minnp = nowindows['Total_NPs'].min(skipna=True)
avgnp = nowindows['Total_NPs'].mean(skipna=True)

print("Calculating Stats for Windows...")

#add row for total windows
data.append(pd.Series(name='Total_Windows'))
data.loc['Total_Windows'] = data.sum(axis = 0)

#set start/stop/NPs totals to None
data.at['Total_Windows', 'start'] = None
data.at['Total_Windows', 'stop'] = None
data.at['Total_Windows', 'Total_NPs'] = None

#get max min mean of windows
maxwin = data.loc['Total_Windows'].max(skipna=True)
minwin = data.loc['Total_Windows'].min(skipna=True)
avgwin = data.loc['Total_Windows'].mean(skipna=True)

#nowindows.to_csv(out2)


print("\n\nThere are " + str(windows) + " genomic windows in this sample.")
print("There are " + str(nps)+ " NPs in this sample.")
print("The maximum number of windows present in an NP is " + str(maxwin))
print("The mininum number of windows present in an NP is " + str(minwin))
print("The average number of windows present in an NP is " + str(int(avgwin)))
print("The maximum number of NPs present in a window is " + str(maxnp))
print("The minimum number of NPs present in a window is " + str(minnp))
print("The average number of NPs present in window is " + str(int(avgnp)))
print("\n\n")

#print(data)

data.to_csv(out)