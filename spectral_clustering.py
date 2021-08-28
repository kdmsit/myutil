# Spectral CLustering

from sklearn.cluster import SpectralClustering
def spectral_clustering(adj,num_cluster):
    clustering = SpectralClustering(n_clusters=num_cluster, affinity='precomputed', assign_labels="discretize",
                                    random_state=42).fit(adj)
    return clustering.labels_