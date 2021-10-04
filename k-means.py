import numpy as np

from numpy import linalg as LA
from typing import Iterable, List, Tuple

np.random.seed(seed=0)


def kmeans2d(
    arr: Iterable[Tuple[float, float]], 
    K: int, 
    *, 
    loop: int=300,
    seed: int=0) -> Tuple[List[int], List[Tuple[float, float]]]:
    """
    Given a 2-dimensional array, generate the k-means cluster
    """
    # Update random seed if requested
    if seed:
        np.random.seed(seed=seed)

    # ----- INIT STEP ----- #
    n = len(arr)
    ohe_cluster = np.zeros((n, K))
    # Randomly assign the cluster using one-hot encoding
    for i, j in enumerate(np.random.randint(K, size=(n, 1))):
        ohe_cluster[i][j] = 1

    # ----- ITERATIVE SEARCH ----- #
    l = 0
    while l < loop:
        """ 
                        CLUSTER MEANS 
        Dot product between arr.T and the cluster profile gives the sum_x and sum_y
        for each of the cluster. This is then divided by the count of 1s in the
        each cluster to arrive at the mean
        """
        # Safeguard (1) against zero allocation to one of the clusters
        n_cluster = sum(ohe_cluster).astype(np.float64)
        n_cluster[n_cluster == 0] = np.nan

        # Compute the means of the clusters
        means_cluster = np.divide(np.dot(arr.T, ohe_cluster), n_cluster).T

        # Safeguard (2) to allow the search to continue despite an empty cluster, pick a random centroid
        means_cluster[np.isnan(means_cluster[:, 0]), 0] = np.random.choice(arr[:, 0])
        means_cluster[np.isnan(means_cluster[:, 1]), 1] = np.random.choice(arr[:, 1])

        """        DISTANCE TO MEAN        """
        # Repeat the array values for each of the cluster to vectorize the
        # calculation of the relative distance by dimension
        re_arr = np.reshape(np.repeat(arr, K, axis=0), (n, 2 * K))
        # (xi, yi) - (x_bar, y_bar) for each observation, by cluster
        reldist = re_arr - means_cluster.flatten()
        # Split the combined matrix back into separate clusters to compute the Euclidean distance
        eudist = [0] * K
        for k in range(K):
            eudist[k] = LA.norm(reldist[..., k:k+2], ord=2, axis=1)

        score_cluster = np.array(eudist).T
        # Pick the cluster with the shortest distance for each observation
        min_score = score_cluster.min(axis=1).reshape(n, 1)
        # Generate the cluster profile for the next iteration
        ohe_nxt_cluster = np.array(score_cluster == min_score, dtype=int)

        # Break the loop if steady-state has been achieved
        if (ohe_cluster == ohe_nxt_cluster).all():
            break

        # Update the cluster profile
        ohe_cluster = ohe_nxt_cluster
        l += 1

    # ----- PACKAGING FOR OUTPUT ----- #
    lst_id = [0] * n
    for i, obs in enumerate(ohe_cluster):
        for j, val in enumerate(obs):
            if val:
                lst_id[i] = j
                break

    return lst_id, [tuple(x) for x in means_cluster]


if __name__ == '__main__':
    arr = np.random.random_sample((1000, 2)) * 40 + 10
    print(arr)

    lst_id, centroids = kmeans2d(arr, 5, loop=300, seed=1)

    print(lst_id)

    print(centroids)
