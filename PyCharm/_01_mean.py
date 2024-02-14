import numpy as np

# 배열 선언
A = np.array([1, 2, 3, 4])
print(A)

# mean(평균)
mean = (A[0] + A[1] + A[2] + A[3])/4
print(mean)

# variace(분산)
vari = ((A[0]-mean)**2 + (A[1]-mean)**2 + (A[2]-mean)**2 + (A[3]-mean)**2)/4
print(vari)

# standard deviation (표준편차) : sqrt(square route)
std = np.sqrt(vari)
print(std)

mean = np.mean(A)

