x = int(input("How many candies you want?"))

i = 1

av = 5

while i <= x:
    if i > av:
        print("Out of Stock")
        break
    print("candy", i)
    i += 1


for i in range(1,11):
     if i%3 == 0 or i%5 == 0:
         continue
     print(i)