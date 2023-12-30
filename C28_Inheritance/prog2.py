# Instance variable not only initialize with constructor but also instance methods too but while accessing that instance method we need to create an obj that means constructor implicitly comes into the picture.
class Demo:
    def __init__(self):
        print("Constructor")
        self.x = 10
        self.y = 20
        print(self)
        
    def setData(self, z):
        self.z = z
    
    def printData(self):
        print(self.x, self.y, self.z)
        
    def data():
        print('data')
        
obj = Demo()
print(obj)
obj.setData(30)
obj.printData()

# obj.data()  # TypeError: positional args differ
