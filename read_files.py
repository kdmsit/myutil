# Read Json File with Python
import json
with open('../atom_init.json') as f:
  data = json.load(f)

# Read value from dict object and save into .csv
feat=[]
for k, v in data.items():
  feat.append(v)

import csv
file = open("atom_features.csv", 'w', newline='')
with file:
  wr = csv.writer(file)
  wr.writerows(feat)

# read .mtx file
import scipy as scp
source_adj_path = "../data/polblogs/polblogs.mtx"
adj=scp.io.mmread(source_adj_path).todense()












