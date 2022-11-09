import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors

np.random.seed(0)
cov = np.array([[1,0], [0,1]])
N = 50

# label 0 : red
X0 = np.random.multivariate_normal([3, 3], cov, N)
# 1 : green
X1 = np.random.multivariate_normal([9, 8], cov, N)
# 2 : blue
X2 = np.random.multivariate_normal([7, 4], cov, N)

data = np.concatenate([X0, X1, X2], axis = 0)
res = np.array([0] * 50 + [1] * 50 + [2] * 50)


plt.plot(X0[:, 0], X0[:, 1] , 'ro')
plt.plot(X1[:, 0], X1[:, 1] , 'go')
plt.plot(X2[:, 0], X2[:, 1] , 'bo')

point = np.array([4.5, 2.5])
point1 = np.array([5, 4])
point2 = np.array([6, 10])
point3 = np.array([5.5, 4]) 

plt.plot(point[0], point[1], 'ko')
plt.plot(point1[0], point1[1], 'ko')
plt.plot(point2[0], point2[1], 'ko')
plt.plot(point3[0], point3[1], 'ko')
plt.show()

# from sklearn.model_selection import train_test_split
# data_train, data_test, res_train, res_test = train_test_split(data, res, test_size = 0.1)

clf = neighbors.KNeighborsClassifier(n_neighbors = 20)
clf.fit(data, res)

result = clf.predict([point, point1, point2, point3])

print(result)