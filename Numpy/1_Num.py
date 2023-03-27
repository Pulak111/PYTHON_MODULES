import numpy as np
myarr = np.array([[3, 6, 34, 27], [12,35,37, 48]])
#if we had to make 2d array we need to know that column will be same
# [2,3] throws error as there is only 2 columns here
print(myarr)
print(myarr[1, 3]) # print 3rd(4th element) index colum in 2nd row
print(myarr[1]) # Print the whole row 2
print(myarr.shape) # Total number of row and column
print(myarr.dtype)