class Parent:
    def __init__(self):
        print("parent constructor")
    def __init__(self):
        print("Another Par constructor")
        print(self)

    def parFun(self):
        print("parent function")

# obj = Parent()

class Child(Parent):
    # def __init__(self):
        # print("child constructor")
        # print(self)


        
    def childFun(self):
        print("child function")

obj = Child()
obj.parFun()
print(obj)