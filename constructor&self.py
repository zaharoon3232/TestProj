class Computer:
    def __init__(self):
        self.name = 'Zaid'
        self.age = 31

    def update(self):
        self.age = 30

    def compare(self,c2):
        if self.age == c2.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()



c1.name = 'Haroon'
c1.age = 65

c1.update()

if c1.compare(c2):
    print("they are same")
else:
    print("They are different")

print(id(c1))
print(id(c2))

print(type(c1))


print(c1.name)
print(c2.name)