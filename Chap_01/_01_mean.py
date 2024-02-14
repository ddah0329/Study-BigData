import numpy as np

A = np.array([1, 2, 3, 4])
print(A)

mean = (A[0] + A[1] + A[2] + A[3])/4
print(mean)

vari = ((A[0]-mean)**2 + (A[1]-mean)**2 + (A[2]-mean)**2 + (A[3]-mean)**2)/4
print(vari)