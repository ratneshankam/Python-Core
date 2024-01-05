class object:
    pass

class Demo(object):
    def __init__(self):
        self.x = 10
        super().__init__()
        
class DemoChild(Demo):
    def __init__(self):
        self.y = 20
        super().__init__()

    def printD(self):
        print(self.x, self.y)

obj = DemoChild()        
obj.printD()

print(DemoChild.mro())              # [<class '__main__.DemoChild'>, <class '__main__.Demo'>, <class '__main__.object'>, <class 'object'>]
class type():
    def __init__(self,x):             # self, x <- required
        print("Hello")
        # return "bye"          # TypeError: __init__() should return None, not 'str'
    
print(type(obj))        # TypeError: type.__init__() takes 1 positional argument but 2 were given  