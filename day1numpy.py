import numpy as np
# creating an array using the np.array method
arr=(np.array([1,"hello",2],dtype=object))
print(type(arr))
print(arr)
# creating an array of zeros using np.zeros(shape) method
zeros=np.zeros((2,3),dtype=int)
print(zeros)
# creating an array of ones using np.ones(shape) method
ones=np.ones((3,3),dtype=int)
print(ones)
#creates an array with in the given range 
even=np.arange(0,10,2)
print(even)
#np.linspace  evenly gives spaced numbers btwn the numbers with in the step value
space=np.linspace(1,100,4)
print(space)
space_2=np.linspace(1,2,5)
print(space_2)
#sum method used to return the sum of the elements of array or any two arrays
sum=np.sum([1,2,3,4])
print(sum)
# printing the sum of two arrays 
two_sum=np.sum([[1,2,3],[4,5,6]],axis=0)
print(two_sum)
# axis-->0 to travel in the direction of one column to another column
# axis-->1 to travle in the directions of row
# logic of axis-->1 
n=[[1,2,3],[4,5,6]]
axis_1=[]
for i in range(len(n)):
    sum=0
    for j in range(len(n[i])):
        sum+=n[i][j]
    axis_1.append(sum)
print(axis_1)
# logic of axis--> 0
m=[[1,2,3],[4,5,6]]
axis_0=[]
for col in range(len(m[0])):
    total=0
    for row in range(len(m)):
        total+=m[row][col]
    axis_0.append(total)
print(axis_0)
