import numpy as np;
import matplotlib.pyplot as plt

# np.random.seed(2)

X = np.random.rand(200, 1)
y = 4 + 3 * X + .2 * np.random.rand(200, 1)

plt.plot(X, y, marker = 'o', color = 'blue', ls = '')
plt.plot([0,1], [4, 7], marker = '*', color = 'red', ls = '-')
plt.axis([0,1,0,10])
plt.show()

bias = np.ones([X.shape[0], 1])
bias = bias.reshape(X.shape[0], 1)

print(bias[:5])
print(X[:5])
X = np.concatenate((bias, X), axis = 1)

print(X[:5])
# X = np.concatenate((bias, X), axis = 1)
# print(X[:5])

eta = 0.09

def grad(w):
    N = X.shape[0]
    return 1/N * X.T.dot(X.dot(w) - y)

def loss(w):
    N = X.shape[0]
    return 0.5/N * np.linalg.norm(X.dot(w) - y,2 )**2

w = [[1, 1]]# hand test -> push to loop

print(X.shape)
temp = np.array(w)
temp = temp.reshape([2,1])
res = [temp]

for i in range(1, 1000):
    t = res[-1] - eta * grad(res[-1])
    if loss(t) < 1e-3:
        break
    res.append(t)

print('res:', res[-1])

g = []
h = []

for i in res:
    g.append(i[0][0])
    h.append(i[1][0])

plt.plot(g, h, ls = '', marker = 'o', ms = 5.0)
plt.xlabel('x_axis')
plt.ylabel('y_axis')
plt.title('theta change')
plt.axis([0,8,0,8])
plt.show()