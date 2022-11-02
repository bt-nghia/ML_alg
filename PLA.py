import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2)
cov_mat = [[.3,.2], [.2, .3]]

clas = np.array([1] * 10 + [-1] * 10)
b_set = np.random.multivariate_normal([2,2], cov_mat, 10)
r_set = np.random.multivariate_normal([4,2], cov_mat, 10)

print(b_set.T)
print(r_set.T)

plt.plot(b_set.T[0], b_set.T[1], 'bo')
plt.plot(r_set.T[0], r_set.T[1], 'ro')
plt.axis([0, 6, 0, 6])
# plt.show()
print(clas)
print(clas.shape)
clas = clas.reshape([clas.shape[0], 1])
# print(clas)


X = np.concatenate([b_set, r_set] ,axis = 0)
bias = np.ones([X.shape[0], 1])
X = np.concatenate([bias, X], axis = 1)

w = np.array([1] * 3)
w = w.reshape([3,1])

print(b_set)
print(r_set)
print(X)
print(X.dot(w).shape)

def loss(index):
    lw = clas[index] * X[index].dot(w)
    return  lw

def gradient(index):
    grad = clas[index] * X[index]
    grad = grad.reshape([3, 1])
    # print(grad)
    return grad

def stop(w):
    temp = np.sign(np.dot(X, w))
    # print(temp)
    # print(clas)
    if np.array_equal(temp, clas):
        return True
    return False

eta = 0.1
ans = []

def sgd(w):
    print(w)
    index = np.random.randint(0, 20)
    while True:
        if np.sign(X[index].dot(w)) != clas[index]:
            w = w + gradient(index) * eta
            # w_list.append(w_new)
        index = np.random.randint(0, 20)
        if stop(w):
            ans.append(w)
            break
    print(w)

print(w.shape)
sgd(w)
w = ans[0]
print(w[0,0], w[1, 0], w[2, 0])
plt.plot(b_set.T[0], b_set.T[1], 'bo')
plt.plot(r_set.T[0], r_set.T[1], 'ro')
x_data = [6, 0]
y_data = []

for i in x_data:
    y_data.append((w[0, 0] + w[1, 0] * i) / -w[2, 0])
    
plt.plot(x_data, y_data, color = 'blue' , ls = '-')
plt.axis([0, 6, 0, 6])
plt.show()