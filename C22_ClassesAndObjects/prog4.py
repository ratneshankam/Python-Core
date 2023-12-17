class Employee:
    def __init__(self):
        print("In constructor", self)
        # Instance variable not initialized
        # self.empId
        # self.empName

        self.empId = 12
        self.empName = 'Kanha'
        
    def empInfo(self):
        print(self)
        print(self.empId, self.empName)
        # print(empId, empName)     # NameError
        
obj = Employee()
print(obj)

# print(empId, empName)     # NameError
print(obj.empId, obj.empName)