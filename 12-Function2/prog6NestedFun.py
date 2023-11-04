print("Welcome Function program")

def outer():
    def inner1():
        print("In inner function 1")
    def inner2():
        print("In inner function 2")
        
    print("In outer function")

outer().inner()                 # AttributeError: 'NoneType' object has no attribute 'inner'
