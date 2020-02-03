#Amanda Holbrook
#CS 4900
#Pattern Discovery in 3D Genome Data
#Assignment #2
#ESTIMATING RADIAL POSITION AND CHROMATIN COMPACTION FROM GAM DATA

import pandas as pd
import numpy as np

out = open('results.csv', 'w')

#getting data file into dataframe
infile = input("\n\nInput testing file: ")
print("\n\nReading file...")
data = pd.read_csv(infile, index_col=0, header=0)

# print(list(data))
# print(data.index)

#find mean max min of nps to determine ratings
meannp = data.loc['Total_Windows'].mean()
maxnp = data.loc['Total_Windows'].max()
minnp = data.loc['Total_Windows'].min()

# print("Mean NP: " + str(meannp))
# print("Max NP: " + str(maxnp))
# print("Min NP: " + str(minnp))

npjump = int(maxnp / 5)
zeros = [None] * len(data)

nps = dict(zip(list(data), zeros))
nplist = list(data)

#determine ratings for NPs
for x in nps:
    if x == "start" or x == "stop" or x == "Total_NPs":
        continue
    if data.at["Total_Windows", x] <= npjump:
        nps[x] = 1
    elif data.at["Total_Windows", x] > npjump and data.at["Total_Windows", x] < npjump * 2:
        nps[x] = 2
    elif data.at["Total_Windows", x] > npjump * 2 and data.at["Total_Windows", x] < npjump * 3:
        nps[x] = 3
    elif data.at["Total_Windows", x] > npjump * 3 and data.at["Total_Windows", x] < npjump * 4:
        nps[x] = 4
    elif data.at["Total_Windows", x] > npjump * 4 and data.at["Total_Windows", x] <= maxnp:
        nps[x] = 5

#add NP ratings to dataframe
data.loc["NP_Ratings"] = nps

#find mean max min of windowss to determine ratings
meanwin = data['Total_NPs'].mean()
maxwin = data['Total_NPs'].max()
minwin = data['Total_NPs'].min()

# print("Mean Window: " + str(meanwin))
# print("Max Window: " + str(maxwin))
# print("Min Window: " + str(minwin))

winjump = int(maxwin / 10)
zeros = [None] * (len(list(data.index)))
keys = list()
for x in range(0, len(list(data.index))):
    keys.append(x)

wins = dict(zip(keys, zeros))

n = len(list(data)) - 1

#determine ratings for windows
for x, row in enumerate(data.itertuples(index=False)):
    if x == n or x == n - 1:
        continue
    if data.iloc[x, n] <= winjump:
        wins[x] = 10
    elif data.iloc[x, n] > winjump and data.iloc[x, n] < winjump * 2:
        wins[x] = 9
    elif data.iloc[x, n] > winjump * 2 and data.iloc[x, n] < winjump * 3:
        wins[x] = 9
    elif data.iloc[x, n] > winjump * 3 and data.iloc[x, n] < winjump * 4:
        wins[x] = 7
    elif data.iloc[x, n] > winjump * 4 and data.iloc[x, n] < winjump * 5:
        wins[x] = 6
    elif data.iloc[x, n] > winjump * 5 and data.iloc[x, n] < winjump * 6:
        wins[x] = 5
    elif data.iloc[x, n] > winjump * 6 and data.iloc[x, n] < winjump * 7:
        wins[x] = 4
    elif data.iloc[x, n] > winjump * 7 and data.iloc[x, n] < winjump * 8:
        wins[x] = 3
    elif data.iloc[x, n] > winjump * 8 and data.iloc[x, n] < winjump * 9:
        wins[x] = 2
    elif data.iloc[x, n] > winjump * 9 and data.iloc[x, n] <= maxwin:
        wins[x] = 1

#print(wins)

data["Window_Ratings"] = wins.values()

print(data)
data.to_csv(out)


