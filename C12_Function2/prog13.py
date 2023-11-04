def Outer():
    def inner1(x,y):
        print("in inner1 fun")
        return x+y

    return inner1
    print("In outer")                   # After return statement codes are ignored didn't thorw error
    
# If return nothing means by default -> None

print(Outer()(2,3))