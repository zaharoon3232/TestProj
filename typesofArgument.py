def person(name,age=18):

    print(name)
    print(age)


person('zaid', 31)

person(name='zaid',age =30)

person('zaid')


def sum(x, *y):

    print(x)
    print(y)
    c= x
    for i in y:
        c = c + i
    print(c)



sum(4,5,1,3)


def sum(*y):


    print(y)
    c= 0
    for i in y:
        c = c + i
    print(c)



sum(4,5,2,3)
