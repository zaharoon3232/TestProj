def greet():
    print("Hello")
    print("Good Morning")


def add(x,y):
    z = x+y
    d = x-y
    return z,d


result1,result2 = add(5,6)
print(result1, result2)