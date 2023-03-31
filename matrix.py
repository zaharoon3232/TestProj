from numpy import *

arr = array([
               [1,2,3,2,9,4],
               [4,5,6,7,5,7]

            ])

print(arr)
print(arr.dtype)
print(arr.ndim)
print(arr.shape)
print(arr.size)

arr2 = arr.flatten()

print(arr2)

arr3 = arr2.reshape(3,4)

print(arr3)



