class Laptop:
    def code(self, ide):
        ide.execute()


class PyCharm:

    def execute(self):
        print("Compiling")
        print("Running")


class MyEditor:
    def execute(self):
        print("spell check")
        print("Convention check")
        print("Compiling")
        print("Running")

#ide = PyCharm()

ide = MyEditor()

lap1 = Laptop()
lap1.code(ide)

