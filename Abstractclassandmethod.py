from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print('running')


#com = Computer()
#com.process()

com1 = Laptop()