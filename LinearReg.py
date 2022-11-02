from __future__ import division, print_function, unicode_literals
import numpy as np 
import matplotlib.pyplot as plt

def show_weight_height():
    X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).transpose()
    y = np.array([[ 49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).transpose()

    plt.plot(X, y, 'ro') # ex: ro stand for show point r : red color
    plt.axis([140, 190, 45, 75])
    plt.xlabel('height (cm)')
    plt.ylabel('weight (kg)')
    plt.show()

show_weight_height()

def linearRegression():
    X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).transpose()
    y = np.array([[ 49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).transpose()

    plt.plot(X, y, 'ro') # ex: ro stand for show point r : red color
    plt.axis([140, 190, 45, 75])
    plt.xlabel('height (cm)')
    plt.ylabel('weight (kg)')
    
    # bulid X bar
    one = np.ones((X.shape[0], 1))
    # concate one vs data w0(bias) multiply 1
    Xbar = np.concatenate((one, X), axis = 1)
    
    print(Xbar)
    
    # calculate
    A = np.dot(Xbar.T, Xbar)# multiply
    b = np.dot(Xbar.T, y)
    w = np.dot(np.linalg.pinv(A), b) # linalg : linear, alg pinv: pseudo inverse
    
    print(w)
    w_0 = w[0][0]
    w_1 = w[1][0]
    
    x0 = np.linspace(145, 185, 2)
    
    # weight = w0 + w1 * height
    y0 = w_0 + w_1 * x0
    
    plt.plot(X.transpose(), y. transpose(), 'ro')
    plt.plot(x0, y0)
    plt.axis([140, 190, 45, 75])
    
    plt.show()
    
    
    
linearRegression()