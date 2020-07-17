# Read Json File with Python
import json
with open('../atom_init.json') as f:
  data = json.load(f)
# print(data)


# Read value from dict object and save into .csv
feat=[]
for k, v in data.items():
  feat.append(v)

import csv
file = open("atom_features.csv", 'w', newline='')
with file:
  wr = csv.writer(file)
  wr.writerows(feat)


# Atom Index Features
index_feature=[]
for i in range(len(feat)):
    count = 0
    index = []
    for j in range(len(feat[i])):
        if feat[i][j] == 1:
            count = count + 1
            index.append(j)
    index_feature.append(index)
file = open("atom_index_features.csv", 'w', newline='')
with file:
  wr = csv.writer(file)
  wr.writerows(index_feature)