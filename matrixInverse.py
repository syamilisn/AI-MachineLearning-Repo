# Python program to inverse
# a matrix using numpy

# Import required package
import numpy as np

# Taking a 3 * 3 matrix
A = np.array([[7, 8],[11, 11]])

# Calculating the inverse of the matrix
print(np.linalg.inv(A))
