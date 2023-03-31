a = 10
c =17
x =143
print(id(x))
def something():
    a = 15
    b = 8
    global c
    c=9
    y = globals()['x']
    print(id(y))
    print("in fun",a)
    print("in func",c)

    globals()['x'] = 145
    #print("in function" y)
something()
print(a)
print(c)
print(x)