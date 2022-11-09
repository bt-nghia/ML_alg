import numpy as np
import matplotlib.pyplot as plt
np.random.seed(2)

X = np.array([0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 1.75, 2.00, 2.25, 2.50, 
              2.75, 3.00, 3.25, 3.50, 4.00, 4.25, 4.50, 4.75, 5.00, 5.50])
y = np.array([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1])

plt.plot(X[np.where(y==1)], y[np.where(y==1)], 'bo');
plt.plot(X[np.where(y==0)], y[np.where(y==0)], 'ro');
plt.show()

one = np.ones([20])
X = np.concatenate([X.reshape([20, 1]), one.reshape([20, 1])], axis = 1)
y = y.reshape([20 ,1])
print(X)
print(y)

import math

def sigmoid(x):
    return 1 / (1 + pow(math.e, -x))

print(math.e)

eta = 0.05

def logistic_regression(X, y):
    w = np.ones([2,1])
#     print(w)
    for i in range(10000):
        index = np.random.randint(0, X.shape[0], 10)
        for i in index:
            xi = X[i].reshape([1,2])
            yi = y[i]
            zi = sigmoid(xi.dot(w))
#             print("xi",xi)
#             print("yi",yi)
#             print("zi",zi)
#             print("xi * w", xi * w)
            w = w + (yi-zi) * eta * np.array(xi).reshape([2,1])
    return w

w = logistic_regression(X, y)
print(w)

temp1 = np.array([[1.],[1.]])
temp2 = np.array([4.75, 1.  ]).reshape([1,2])
print("temp1.shape: ", temp1.shape)
print("temp2.shape: ", temp2.shape)
print()
print((temp2.dot(temp1)).shape)
# print(temp2.dot(temp1))

print((temp2 * temp1).shape)

plt.plot(X.dot(w)[np.where(y==1)], y[np.where(y==1)], 'bo');
plt.plot(X.dot(w)[np.where(y==0)], y[np.where(y==0)], 'ro');

temp_x = np.linspace(-3, 6, 1000)
temp_y = []
for i in temp_x:
    temp_y.append(sigmoid(w[0][0] * i + w[1][0]))
temp_y = np.array(temp_y)
plt.plot(temp_x, temp_y, 'g-');
plt.show()