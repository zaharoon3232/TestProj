class A:
    def __init__(self):
        print("in A Init")
    def feature1(self):
        print("feature 1 working")

    def feature2(self):
            print("feature 2 working")

class B(A):
    def __init__(self):
        #super().__init__()
        print("in B Init")

    def feature3(self):
            print("feature 3 working")

    def feature4(self):
            print("feature 4 working")

a1 = A()
a1.feature1()

b1 = B()





