import numpy as np

# # program to equal the length of all the subarrays of a array
a=[[1,2,3],[4,5],[6,7,8,9]]
max_row=0
for i in range(len(a)):
    if len(a[i])>max_row:
        max_row=len(a[i])
for i in a:
    while len(i)<max_row:
        i.append(0)
print(a)
print(np.sum(a,axis=0))

# # mean : It returns the average of the array in the axis that we give
array=[[1,2,3],
       [4,5,6],
       [7,8,9]]
res=np.mean(array,axis=1,dtype=int)
print(res)

# # median: It returns the middle value of an array 
array=[[1,2,3],
       [4,5,6],
       [7,8,9]]
array=np.array(array)
refined=array.flatten()
mid=np.median(refined.astype(np.int64))
print(mid)

a=[1,2,3,4,5,6]
mid=len(a)//2
if len(a)%2==0:
    add=a[mid]+a[mid-1]
    print(add/2)
else:
    print(a[mid])
    
# reshape:it changes the shape or dimensions of the array as per requirement

b=[1,2,3,4]
print(np.reshape(b,(2,2)))
print(np.reshape(np.arange(12),(2,2,3)))

#flatten : it is used to break down the nested arrays into 1 dimensional array

print(np.reshape(np.arange(12),(6,2))).flatten()

# concatenate :It is used to merge two arrays of same length

a=np.array([1,2])
b=np.array([3,4])
print(np.concatenate((a,b)))

# where condition : returns the index values of the elements that matches our condition

num=np.array([12,32,8,7,5])
print(np.where(num%2==0))
print(np.where(num<10))
print(np.where(num==33))

u=np.array([[10,10,30],[50,99,990]])
print(np.where(u%10 ==0))

# unique : it returns all the unique elements for once after sorting the array

l=["a","b","c","d","a","b","d"]
print(np.unique(l))

# print the idex and value of the given number (where logic)
a=[[1,2,3],
   [3,6,5]
   ]
num=5
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j]==num:
            print(f"the num {num} is found at [{i},{j}]")
