a = 5
b = 2



try:
    print("Resource Open")
    print(a/b)

    k = int(input("Enter a number"))
    print(k)

except ZeroDivisionError as e:
    print("Hey, you cannot divide a number by zero")

except ValueError as e:
    print("Invalid Input")

except Exception as e:
    print(e)

finally:
    print("Resource closed")

print("Bye")
