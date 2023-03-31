def check(lst):

    even = 0
    odd= 0
    for i in lst:
        if i%2 == 0:
            even +=1
        else:
            odd +=1

    return even,odd


lst = [10,25,14,24,18,47,30]

even,odd = check(lst)

print(even,odd)
print("Even: {} and Odd: {}".format(even,odd))