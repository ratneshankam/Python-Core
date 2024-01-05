print("Start code")
class Demo:
    def __init__(self):
        print("In constructor")
    
    def __del__(self):
        print("In destructor")

obj1 = Demo()
obj2 = Demo()
# GC checks reference count [must be 0 to delete an object]
obj3 = obj1                 # It's creating another reference to an object Demo()
del obj1


print("End code")