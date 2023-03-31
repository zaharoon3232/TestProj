class Car:
    wheels = 4
    def __init__(self):
        self.mil = 10
        self.com = "BMW"


c1 = Car()
c2 = Car()

print(c1.mil, c1.com, c1.wheels)

print(Car.wheels)

Car.wheels = 8

print(c1.wheels)
print(Car.wheels)