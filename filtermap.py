from functools import reduce
#def is_even(a):
 #   return a%2==0




nums = [3,4,5,2,6,8,10,11,14,9]

#evens = list(filter(is_even,nums))
#print(evens)


evens = list(filter(lambda a:a%2==0, nums))

doubles = list(map(lambda n: n*2,evens))

sum = reduce(lambda n,m:n+m,doubles)
print(evens)

print(doubles)
print(sum)