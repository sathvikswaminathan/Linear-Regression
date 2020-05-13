# There are multiple ways of implementing Least Squares

# The Calculus way : 

## Gradient Descent :
Gradient Descent has been implemented on the mean squared error function

### The following image is a graph between the cost function and the number of steps taken by the parameter x.

![alt tag](https://github.com/sathvikswaminathan/Linear-Regression/raw/master/Linear%20Regression/Gradient%20Descent/gradient_descent.png)

# The Linear Algebra way :

The matrix representation of a system of linear equations is of the form **Ax = b** . 

The above equation can be solved without any hassle if **b** belongs to the column space of **A**. If **b** does not belong to the column space of **A** then the equation cannot be solved. The following algorithms can be used to compute an approximate solution in such cases.

## i) Normal Solution :
The operation used to compute the Normal Solution is the following:

**x = (A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>b**

This solution can be obtained by projecting the vector **b** onto the column space of **A** (**p**) and then solving for **x**
using the equation **Ax<sup>^</sup> = p**, where **x<sup>^</sup>** is the approximate solution.

This solution can also be obtained by taking the derivative of square of the magnitude of the error vector i.e. **b-Ax<sup>^</sup>**
and setting it to **0**.

## ii) Gram Schmidt :

This is similar to the Normal Solution. An orthogonal basis for the column space is computed using the  Gram Schmidt algorithm to make certain computations like the inverse of a matrix less expensive. A matrix can be decomposed into an orthogonal matrix **Q** and an upper triangular matrix **R**.

**A = QR** (QR Factorization)

Orthogonal Matrices also have the following property which is computationally convinient:

**Q<sup>T</sup>Q = I**

It is always ideal to have an orthogonal basis as it simplifies matrix operations.

## iii) Pseudo Inverse :
The matrix representation of a system of linear equations is of the form **Ax = b** . 

Why not simply solve for **x** by taking the inverse of **A** and multiply it with the **b** vector? 

It's because in most cases **A** is not a square matrix and for an inverse to exist, the Matrix must be a square matrix and it's rank must be equal to its dimensions. 

In the case of a rectangular matrix which has independent columns, we can compute its pseduo inverse by decomposing it using **Singular Value Decomposition (SVD)**. 

The Pseduo inverse of a matrix **A** is denoted by **A<sup>+</sup>** . 
**x** can then be computed by the following transformation:

**x** = **A<sup>+</sup> b**.

## Implementing Least Squares the Linear Algebra way comes with its own advantages and disadvantages. 

### Advantages:

#### (My beliefs)
* It is a non-iterative algorithm. Unlike gradient descent, this algorithm does not have to train the model in an interative manner to predict results.
* The equation to compute the Normal solution comes in a very compact form. Irrespective of the number of features, the equation remains the same as all of the information is packed into a Matrix.

## Then why use Gradient Descent?

### Disadvantages: 
The Normal solution is preferred in every case in which it is not too computationally expensive to compute.

If the data points and the training feautures are large in number (sometimes in a machine learning algorithm we can end up with number of data points >1,000,000 and number of variables > 1000), the size of the Matrix becomes huge and it becomes computationally expensive to even initialize the matrix and on top of that a lot of expensive operations have to be performed on the matrix.

In such scenarios the gradient descent algorithm is computationally less expensive and saves a lot of time on calculations.
