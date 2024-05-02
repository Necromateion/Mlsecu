from sklearn.datasets import make_blobs

def get_distributions(centers, cluster_std, n_samples):
    X, y = make_blobs(n_samples=n_samples, centers=centers, cluster_std=cluster_std, random_state=0)
    return X, y

