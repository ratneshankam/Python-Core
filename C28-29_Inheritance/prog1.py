class Parent:
    def __init__(self):
        print("Parent Constructor")
        print(id(self.__init__))
        
    def parentFun():
        print("parent function")

class Child(Parent):
    def __init__(self):
        print("child constructor")
        print(id(self.__init__))

    def childFun():
        print("child function")

obj = Child()
print(id(obj))