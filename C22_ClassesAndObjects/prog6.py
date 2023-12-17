class Company:
    compName = 'facebook'           # class/static variable
    def __init__(self):
        print("In constructor")
        # instance variable
        self.empId = 12
        self.empName = 'Kanha'

    # Instance method -> only accessible with obj instance
    def empInfo(self):
        print(self.empId, self.empName, self.compName, Company.compName) 

    @classmethod
    def compInfo(self):
        print(self.compName, Company.compName)      # instance variable is not accessible

    @staticmethod
    def franchiseInfo():            # means it's not actually member of class
        print(Company.compName)     # instance variable is not accessible

obj = Company()
obj.empInfo()

Company().empInfo()           
# Company.empInfo()           # TypeError

obj.compInfo()
Company.compInfo()

obj.franchiseInfo()
Company.franchiseInfo()


