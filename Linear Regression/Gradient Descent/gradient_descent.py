# implementing gradient descent

import numpy as np
import matplotlib.pyplot as plt

# training data

x = np.array([1,2,3,4,5])  # test input
y = np.array([2.625,3.25,3.875,4.5,5.125])  # test output (y = 5x/8 + 2)
costFunctionValue = [] # list to store cost function values
iterations = [] # list to iteration numbers

def gradientDescent(x,y):
    m = c = 0  # Initial values of parameters set to 0.
    num_interations = 1000
    n = len(x)  # No of datasets
    learning_rate = -0.1634

    for i in range(num_interations):
        y_predicted = m*x + c
        md = (1/n)*sum((y-y_predicted)*x)
        cd = (1/n)*sum(y-y_predicted)
        m = m - (learning_rate)*md
        c = c - (learning_rate)*cd
        cost = costFunction(y_predicted,y,n)
        costFunctionValue.append(cost)
        iterations.append(i)
        print("m = {}, c = {}, iteration_number = {}, cost = {}".format(m,c,i+1,cost))


# defining the cost function
def costFunction(y_predicted,y,m):
    j = (1/(2*m))*sum((y-y_predicted)**2)
    return j


# defining function to plot graph between cost function and iteration number
def plot_graph():
    plt.plot(iterations,costFunctionValue)
    plt.xlabel('iteration_number')
    plt.ylabel('Cost function value')
    plt.title('Cost function Vs Iteration number')
    plt.show()
    plt.savefig('plot.png')

gradientDescent(x,y)

plot_graph()