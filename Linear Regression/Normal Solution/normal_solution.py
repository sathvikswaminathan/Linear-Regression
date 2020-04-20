# Implementing Regression using the Normal Solution Algorithm.
# PROs: It is a non-iterative algorithm and hence it is faster than 
# iterative algorithms such as the gradient-descent algorithm. 

import numpy as np

# y = m1*x1 + m2*x2 + m3*x3 +.....+ c
# number of independent variables (x1, x2, x3..,xn)
num_indep = 2

# training data 
# INPUT
x = [[1,1,3,4],[1,2,4,6]] 
# OUTPUT
y = [2,3,8,12]

input_size = len(x[0])
for vector in x:
	if len(vector) != input_size or len(vector) != len(y): 
	    exit() 

# converting to 2-D numpy array
y = np.array([y])
# TODO: take y transpose
y_transpose = y.transpose()

# dimensions of matrix A (m x n):
m = len(x[0])
n = num_indep + 1

# defining the matrix A
A = []
for i in range(m):
	row = []
	for vector in x:
		row.append(vector[i])
	row.append(1)
	A.append(row)

# converting to numpy array
A = np.array(A)

# algorithm to find the normal solution
A_transpose = A.transpose()
# B and C are just intermediate matrices to compute the final vector (params)
B = np.linalg.inv(np.matmul(A_transpose, A))
C = np.matmul(A_transpose, y_transpose)

params = np.matmul(B, C) # will contain m1, m2, m3, m4, ...., c

equation = 'y = '

for i in range(len(x)):
	equation += str(float(params[i])) + " x" + str(i+1) + " + "

equation += str(float(params[-1]))

print(equation)