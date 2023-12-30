class Parent:
    z = 30
    def __init__(self):
        print("parent constructor")
        self.x = 10
    
    def dispData(self):
        print("par instance-method")
        print(self.x, self.z)
    
    print(id(dispData))         # 100

    @classmethod
    def parData(cls):
        print("par class-method")
        print(cls.z)

    print(id(parData))          # 200

    # Destructor
    def __del__(self):                      # It always get called after code is ended or current object is override
        print("In destructor")

        
class Child(Parent):
    pass

obj = Child()
obj.dispData()
obj.parData()
print(id(obj.dispData), id(obj.parData))        # -> 300 300

