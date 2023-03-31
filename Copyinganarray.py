from numpy import *

arr = array([1,2,3,4,5])

arr = arr + 5

print(arr)

arr2 = array([6,7,8,9,10])

arr3 = arr + arr2

print(arr3)


#print(sin(arr3))
#print(log(arr3))
#print(sqrt(arr3))

print(concatenate([arr, arr3]))

arr4 = arr3.view()

print(arr4)
print(arr3)

print(id(arr4))
print(id(arr3))
