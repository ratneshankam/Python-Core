def Outer():
    def inner1():
        print("In inner1")
    def inner2():
        print("In inner2")
        
    return inner1, inner2


in1, in2 = Outer()

in1()
in2()
################# Another way ####################

retObj = Outer()

for i in retObj:
    i()