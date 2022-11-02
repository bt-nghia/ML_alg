from __future__ import print_function 
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
np.random.seed(11)

centers = np.array([[2, 2], [8, 3], [3, 6]])
print(centers.shape)
cov = [[1, 0], [0, 1]]
N = 500
X0 = np.random.multivariate_normal(centers[0], cov, N)
X1 = np.random.multivariate_normal(centers[1], cov, N)
X2 = np.random.multivariate_normal(centers[2], cov, N)

X = np.concatenate((X0, X1, X2), axis = 0)
print(X.shape[0], X.shape[1])
K = 3

original_label = np.asarray([0]*N + [1]*N + [2]*N).T

def kmeans_display(X, label, center):
    K = np.amax(label) + 1
    X0 = X[label == 0, :]
    X1 = X[label == 1, :]
    X2 = X[label == 2, :]
    
    plt.plot(X0[:, 0], X0[:, 1], 'b^', markersize = 4, alpha = .8)
    plt.plot(X1[:, 0], X1[:, 1], 'go', markersize = 4, alpha = .8)
    plt.plot(X2[:, 0], X2[:, 1], 'rs', markersize = 4, alpha = .8)
    print(center)
    plt.plot(center[0, 0 : ], center[1, 0 : ], 'yo')

    plt.axis('equal')
    plt.plot()
    plt.show()
    
kmeans_display(X, original_label, centers.transpose())

def kmeans_init_centers(X, k):
    return X[np.random.choice(X.shape[0], k, replace = False)]

def kmeans_assign_labels(X, centers):
    # distance btw centers and point 
    D = cdist(X, centers)
    # return index of closet center
    return np.argmin(D, axis = 1)

def kmeans_update_centers(X, labels, K):
    centers = np.zeros((K, X.shape[1]))
    for k in range(K):
        # collect point assign to the k_th cluster
        xk = X[labels == k, : ]
        # take average
        # np.mean return the average of array
        centers[k, :] = np.mean(xk, axis = 0)
    return centers

def has_converged(centers, new_centers):
    # check two sets of centers are the same
    return (set([tuple(a) for a in centers])) == (set([tuple(a) for a in new_centers]))

# core
def kmeans(X, K):
    centers = [kmeans_init_centers(X, K)]
    labels = []
    it = 0
    while 1:
        labels.append(kmeans_assign_labels(X, centers[-1]))
        new_center = kmeans_update_centers(X, labels[-1], K)
        if has_converged(centers[-1], new_center):
            break
        centers.append(new_center)
        it+=1
    return (centers, labels, it)

(centers, labels, it) = kmeans(X, K)
print(centers[-1])

c = centers[-1].transpose()
# print(c)


kmeans_display(X, labels[-1], c)