def update(x):
    print(id(x))
    x = 8
    print(id(x))
    print("x",x)

a = 10
print(id(a))
update(a)
print("a",a)


def updates(lst):
    print(id(lst))
    lst[1] = 8
    print(id(lst))
    print("x",lst)

lst = [10,2,5]
print(id(lst))
updates(lst)
print("a",lst)


