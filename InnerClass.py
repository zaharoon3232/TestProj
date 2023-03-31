class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()


    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:
        def __int__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8
        def show(self):
            print(self.brand)

s1 = Student("Zaid", 3232)

s1.show()

lap1 = Student.Laptop()



