import numpy as np
myarr = np.array([[3, 6, 34, 27], [12,35,37, 48]])
#if we had to make 2d array we need to know that column will be same
# [2,3] throws error as there is only 2 columns here
print(myarr)
print(myarr[1, 1])
print(myarr[0])
print(myarr.shape)
print(myarr.dtype)