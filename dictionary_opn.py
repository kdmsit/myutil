# Check dict for keys and increase count
def count_inc_key(full_dataset):
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
def iterate_dict(data_dict):
    y=[]
    for key, val in data_dict.items():
        y.append(val)