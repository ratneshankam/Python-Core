class Company:
    compName = 'facebook'           # class/static variable
    def __init__(self, empId=0, empName=None):
        print("In constructor", self)
        # Instance variable not initialized (AttributeError)
        # self.empId
        # self.empName

        self.empId = empId
        self.empName = empName
        
    def empInfo(self):
        # print(self)
        print(self.empId, self.empName)
        # print(empId, empName, compName)     # NameError
        # print(Company.empId)                  # AttributeError -> instance variable can't be access by className as it is only in obj namespace

        print(self.compName, Company.compName)          # As class variables are in both class and obj namespaces
        
# obj = Company()
obj = Company(12,'Kanha')
obj1 = Company(15, 'Ashish')
# print(obj)

# print(empId, empName, compName)     # NameError
# print(Company.empId, Company.empName)     # AttributeError
print(obj.empId, obj.empName, obj.compName, Company.compName)

obj.empInfo()
obj1.empInfo()

obj.empId = 10
obj.empName = 'ram'
Company.compName = 'Google'             # (change in class namespace) that change occured in every obj namespace
obj.empInfo()
obj1.empInfo()
# obj namespace change is only for that instance
obj.compName = 'Meta'
obj.empInfo()
obj1.empInfo()



# If something not found in class got -> AttributeError else in outside got -> NameError
# for example ---->
# obj.run()     
# run()