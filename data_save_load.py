# Numpy Load and Save
import numpy as np
def np_load_save(a):
    np.save("a.npy",a)
    data = np.load('a.npy')


# Pickle Save and Load
import pickle as pkl
def pickel_save_load(sentences):
    pkl_out=open("data","wb")
    pkl.dump(sentences,pkl_out)
    pkl_out.close()

    with open("data", 'rb') as handle:
        sentences = pkl.load(handle)