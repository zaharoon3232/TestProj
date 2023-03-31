class Computer:

    def __init__(self, cpu,ram):
        print("in init")
        self.cpu=cpu
        self.ram = ram



    def conf(self):
       #print("i5, 16gb, 500ssd")
        print(self.cpu,self.ram)


com1 = Computer('i5',16)
com2 = Computer('i3',8)
#print(type(com1))

Computer.conf(com1)
Computer.conf(com2)

com1.conf()
com2.conf()