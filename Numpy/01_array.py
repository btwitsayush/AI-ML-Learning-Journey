# Numpy is similar to list in python. But it has several benefits

# 1)Uses Less Memory
# 2)It is fast compare to list
# 3)It is more convinient


import numpy as np

# 1-D array

a1=np.array([1,2,3,4])
a2=np.array([5,6,7,8])

sum=a1+a2
mul=a1*a2
sub=a1-a2

# print(sum)
# print(mul)
# print(sub)

# 2-D array

a3=np.array([[1,2],[4,5],[5,6]])
# print(a3)
# print(a3.ndim) #it will tell the dimension of array

# print(a3.itemsize) #it will tell how many bytes its using

# print(a3.size) #tells total number of array
# print(a3.shape) #tell about no. of rows and columns in it
# print(a3.reshape(2,3)) #it will reshape the array into 2 rows 3 columns

# to create a array of zeroes only of different shape

a4=np.zeros( (3,4))
# print(a4)

# print(a4.ravel())# to convert a array into 1-D and it returns a new array

print(a3.min()) #print min array
print(a3.max()) #print max array
print(a3.sum())#it will sum all of the numbers

# if you want to sum axis in rows or column then we will use axis
print(a3.sum(axis=0))#aixs 0 = rows
print(a3.sum(axis=1))#axis 1 =columns