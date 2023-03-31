x = 8
r = x % 2
if r==0:
    print("Even")
    print("Im always right")
print("Bye")

y = 8
c = y % 2
if c==0:
    print("Even")
    if x>5:
        print("Great")
    else:
        print("not so Great")
else:
    print("Odd")