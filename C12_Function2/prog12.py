def Outer():
    def inner1(a,b):
        print("In inner1")
        return a+b

    def inner2(a,b):
        print("In inner1")
        return a*b
    
    return inner1, inner2

in1, in2 = Outer()

retv1, retv2 = in1(2,4), in2(3,5)

print(retv1 + retv2)

print(in1, in2)