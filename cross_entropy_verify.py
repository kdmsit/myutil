import os
import csv
import numpy as np
import matplotlib.pyplot as plt
from pymatgen.core.structure import Structure
import torch

# property="band_gap"
# print(property)
# property_list=["formation_energy_per_atom","band_gap","efermi","volume","total_magnetization"]
# idx=property_list.index(property)
# id_prop_file = os.path.join('../data/id_prop.csv')
# with open(id_prop_file) as f:
#     reader = csv.reader(f)
#     id_prop_data = []
#     for row in reader:
#         if row[idx+1] != 'None':
#             if 5>=float(row[idx+1])>=0:
#                 id_prop_data.append(float(row[idx+1]))
#
# # print(id_prop_data)
# print(len(id_prop_data))
# print("Property Min",np.min(id_prop_data))
# print("Property Max",np.max(id_prop_data))
# print("Property Mean",np.mean(id_prop_data))
# print("Property Variance",np.var(id_prop_data))
# print("Property Stdev",np.std(id_prop_data))
#
# plt.hist(id_prop_data)
# plt.title(property)
# plt.show()


# del_index=[0,1]
# del_index=range(1,3)
# a = np.arange(16).reshape(4, 4)
# print(a)
# a_del=np.delete(a,del_index , 1)
# print(a_del)


# graphs = dict()
# for i in range(100):
#     print(i)
#     crystal = Structure.from_file(os.path.join("../data/",str(i)+'.cif'))
#     nodes =range(crystal.num_sites)
#     neighbors = crystal.get_all_neighbors(8, include_index=True)
#     graphs[i] = (nodes, neighbors)
# np.savez_compressed('graph_data.npz', graph_dict=graphs)

# x = torch.rand(2, 2)
# y = torch.rand(2, 2)
# z = x*y
# print(x)
# print(y)
# print(z)

# import numpy as np
#
# file_path='../oqmd_dataset/graph_data.npz'
# try:
#     graphs = np.load(file_path,allow_pickle=True)
#     graphs = graphs['graph_dict'].item()
# except UnicodeError:
#     graphs = np.load(file_path,allow_pickle=True, encoding='latin1')['graph_dict'].item()
#     # graphs = {k.decode(): v for k, v in graphs.items()}
#     count=0
#     for k, v in graphs.items():
#         count=count+1
#         print(k.decode(),v)
#     print(count)


# def plot_hist(data_list,filepath):
#     data = data_list
#     plt.ylim(0, 4000)
#     plt.bar(data.keys(), data.values(), 2, color='g')
#     plt.title('Number of atoms in primitive unit cell ')
#     plt.xlabel('Number of atoms ')
#     plt.ylabel('count')
#     plt.savefig(filepath)
#     plt.close()
#
# from data import *
# data_path = '../data/'
# radius=8
# max_num_nbr = 12
# full_dataset = CIFData(data_path,max_num_nbr,radius)
# datasize=len(full_dataset)
# print(datasize)
# noofelements={}
# for i in range(datasize):
#     print(i)
#     sample_data =full_dataset[i]
#     atom_count=len(sample_data[3])
#     if atom_count in noofelements.keys():
#         noofelements[atom_count]=noofelements[atom_count]+1
#     else:
#         noofelements[atom_count] =1
# plot_hist(noofelements,"../results/element.png")

import pandas as pd
mae=[]
data_path='fetched_data.csv'
data=pd.read_csv(data_path,header=None).values
data_length=len(data)
for i in range(data_length):
    fo_o=data[i][1]
    fo_dft = data[i][2]
    ae=abs(fo_o-fo_dft)
    mae.append(ae)
print(np.mean(mae))







































