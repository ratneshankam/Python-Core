# Multiple Inheritance: (mro -> method order resolution)  [thumb rule (right to left)]

class Parent1:
    def __init__(self):
        print("par1 constructor")
    
    def dispData(self):
        print("par1 dispD method")


class Parent2:
    def __init__(self):
        print("par2 constructor")
    
    def printData(self):
        print("par2 printD method")


class Child(Parent2, Parent1):          # parent2 constructor get's called if not exist as per mro parent1 constructor then get's called
    pass

obj = Child()
obj.dispData()
obj.printData()

print(Child.mro())
print(Child.__mro__)