def Outer(x,y):
    def Inner():
        print("In inner function")
    print("In outer fun")
    print(id(Inner))
    return Inner

retval = Outer(2,3)
print(id(retval))           # returns address

# Inner function can call outside like this 
print(retval())