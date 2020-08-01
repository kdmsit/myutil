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



# Tsne Plot

import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
def tsneplot(embeddings,labels,fig_path):
    print("********************* tSNE Plot*********************")
    X = TSNE(n_components=2,perplexity=100,n_iter=1000).fit_transform(embeddings)
    colors = ['#FF0000', '#06D506', '#0931F7', '#00FFFF', '#FFE500', '#F700FF', '#9300FF', '#FFD700','#10DADE']   # Red , Green, Blue
    for c in range(len(colors)):
        points = []
        for j in range(len(labels)):
            if (labels[j] == c):
                points.append(list(X[j]))
        x = []
        y = []
        for z in points:
            x.append(z[0])
            y.append(z[1])
        plt.plot(x, y, 'ro', c=colors[c], markersize=20, marker='.')
    plt.axis('off')
    plt.savefig(fig_path)
    plt.close()

# Spectral CLustering

from sklearn.cluster import SpectralClustering
def spectral_clustering(adj,num_cluster):
    clustering = SpectralClustering(n_clusters=num_cluster, affinity='precomputed', assign_labels="discretize",
                                    random_state=42).fit(adj)
    return clustering.labels_

# read .mtx file
import scipy as scp
source_adj_path = "../data/polblogs/polblogs.mtx"
adj=scp.io.mmread(source_adj_path).todense()



# Check dict for keys and increase count
num_sites_dict={}
    for i in range():
        structures, targets, _,num_sites = full_dataset[0]
        if num_sites in num_sites_dict:
            num_sites_dict[num_sites]=+1
        else:
            num_sites_dict[num_sites]=1

# Sort Dictionary based on key values :
import collections
d = {2:3, 1:89, 4:5, 3:0}
od = collections.OrderedDict(sorted(d.items()))


# Iterate Dictionary
for key, val in num_sites_dict_key_sorted.items():
    y.append(val)


# Numpy Load and Save
np.save("../data/num_sites_count",num_sites_dict_key_sorted)


# Pickle Save and Load
pkl_out=open("../data/"+str(args.data)+"/sentences","wb")
        pkl.dump(sentences,pkl_out)
        pkl_out.close()

with open("../data/"+str(args.data)+"/sentences", 'rb') as handle:
    sentences = pkl.load(handle)


# Torch Tensor Copy
cluster_emb=x.clone() # x is a tensor


