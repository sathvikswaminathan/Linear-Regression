# There are multiple ways of implementing Least Squares
# i) Gradient Descent
Gradient Descent has been implemented on the mean squared error function

## The following image is a graph between the cost function and the number of steps taken by the parameter x.

![alt tag](https://github.com/sathvikswaminathan/Linear-Regression/raw/master/Linear%20Regression/Gradient%20Descent/gradient_descent.png)

# ii) Normal Solution
![alt tag](https://github.com/sathvikswaminathan/Linear-Regression/raw/master/Linear%20Regression/Normal%20Solution/normal_solution.png)

## Implementing the Normal Solution comes with its own advantages and disadvantages. 
### Advantages:
#### (My beliefs)
* It is a non-iterative algorithm. Unlike gradient descent, this algorithm does not have to train the model in an interative manner to predict results.
* The equation to compute the Normal solution comes in a very compact form. Irrespective of the number of features, the equation remains the same as all of the information is packed into a Matrix.

## Then why use Gradient Descent?
### Disadvantages: 
The Normal solution is preferred in every case in which it is not too computationally expensive to compute.
* If the data points and the training feautures are large in number (sometimes in a machine learning algorithm we can end up with number of data points >1,000,000 and number of variables > 1000), the size of the Matrix becomes huge and it becomes computationally expensive to even initialize the matrix and on top of that a lot of expensive operations have to be performed on the matrix.
* In such scenarios the gradient descent algorithm is computationally less expensive and saves a lot of time on calculations.
