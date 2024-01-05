# This single entity/obj (which is not complex) store in common memory area are behaves like scp(string constant pool) in java which share same memory for same obj name or value

class Parent:
    z = 30
    def __init__(self):
        print("parent constructor")
        self.x = 10
        self.y = 20
        # self.z = 100
    
    def dispData(self):
        print("par instance-method")
        print(self.x, self.y, self.z, Parent.z)
            
class Child(Parent):
    def __init__(self):
        print("child constructor")
        # super().__init__()
        self.x = 30
        self.y = 40
        self.z = 50         # Child->self instance variable
        super().__init__()
        # Parent.__init__(self)       # try Child in-place of Child
        
    def childData(self):
        print("par instance-method")
        print(self.x, self.y, self.z, Child.z, Parent.z)

obj = Child()
obj.dispData()
obj.childData()

print(obj, Child)