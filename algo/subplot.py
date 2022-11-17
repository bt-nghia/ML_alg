import matplotlib.pyplot as plt
import numpy as np

X = np.array([1,2,3])
y = np.array([4,5,6])

plt.subplot(3,3,1)
plt.plot([X, y])


X_1 = np.array([2,3])
y_1 = np.array([4,5])
plt.subplot(3,3,4)
plt.plot(X_1, y_1)

plt.subplot(3,3,3)
plt.barh(X_1, y_1)

plt.subplot(3,3,2)
plt.bar(X_1, y_1)

plt.subplot(3,3,5)
explo = [0.2, 0, 0 ,0]
plt.pie([10,20,30,40], explode= explo, shadow= True)

plt.subplot(3,3,6)
temp = np.random.randint(0, 100 , 1000)
plt.hist(temp)
print(temp)
plt.show()