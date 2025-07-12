# clip, np.dot(a1,a2),Transpose,np.inverse,np.random.randn, shape, .ndim,.size

import numpy as np
from numpy import linalg as la

a=np.array([1,2,3,4,5,6,7,8])
print(a)
# clip :it is used to create an array with elements within the given range 
print(np.clip(a,4,8))

# # np.dot : In general this method is used for matrix multiplication
a1=[12,6]
a2=[3,6]
mul=np.dot(a1,a2)
print(mul)

# Transpose :It is used to flip the axis of the array just like swaping the x axis and y axis
t=np.array([[1,2,3],
            [5,6,7],
            [9,8,1]])
print(np.transpose(t))

#inverse: it returns the inverse of a squared matrix and that matrix should contain equal number of rows and columns
i=np.array([[8,7],
            [6,5]])
i_inv=np.linalg.inv(i)
print(i_inv)

#random.randn: it generates the random values and we can even set the dimensions to that matrix
print(np.random.randn(4))
print(np.random.randn(2,3))

#shape : It returns the shape of the array 
p=(np.array([[1,2,3],[4,5,6]]))
print(p.shape)

# .dim:It returns the dimensions of the array
print(np.array([1,2,3]).ndim)
print(np.array([[4,5,7],[8,9,6]]).ndim)

# .size: It returns the size of the array (no:of elements present in the array )
print(np.array([[2,3,4],[6,7,8]]).size)


# Transpose logic
mine=[[1,2,3],
      [4,5,6],
      [7,8,9]]
transpose=[]
for i in range(len(mine[0])):
    row=[]
    for j in range(len(mine)):
        row.append(mine[j][i])
    transpose.append(row)
print(transpose)

is_transposed=np.transpose(mine)
print(is_transposed)

# index logic 
num=8
for i in range(len(mine)):
    for j in range(len(mine[0])):
        if mine[i][j]==num:
            print(f"the {num} is found at row {i+1}, column {j+1}")

# dot logic (matrix multiplications)
a1=[12,6]
a2=[3,6]
multiply=0
for i in range(len(a1)):
     multiply+=a1[i]*a2[i]
print(multiply)

        
