from decisionTree import *
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    data = np.array([1,2,3,34,4])
    label = np.array([0,1,0,1,1])
    plt.subplot(1,1,1)
    plt.plot(data, label, 'bo')
    plt.show()