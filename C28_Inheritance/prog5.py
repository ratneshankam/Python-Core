class Parent:
    z = 30
    def __init__(self):
        print("parent constructor")
        self.x = 10
    
    def dispData(self):
        print("par instance-method")
        print(self.x, self.z)
    
    @classmethod
    def parData(cls):
        print("par class-method")
        print(cls.z)

    # Destructor
    def __del__(self):                      # It always get called after code is ended or current object is override
        print("In destructor")

obj = Parent()
obj = Parent()                  # Overriding destructor called scenario
# obj1 = Parent()

obj.dispData()
obj.parData()

# This methods can called explicitly
obj.__del__()           # Just called method not actually deletes obj
obj.__init__()

obj.dispData()

# del obj         # manually or forcefully called del obj (tell GC that obj not required further) like finalize in java

# obj.dispData()          # NameError: obj not defined

print("End Code")
