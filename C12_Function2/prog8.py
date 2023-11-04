# Outer()       # --> NameError: name 'Outer' is not defined. Did you mean: 'iter'?
def Outer():
    # Inner()       # --> UnboundLocalError: cannot access local variable 'Inner' where it is not associated with a value
    
    def Inner():
        print("Inner function")
    Inner()
    print("Outer function")

print("Start Code")

Outer()

print("End code")