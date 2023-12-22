def outer():
    print("In outer function")
    def inner1():
        print("In inner1 function")
    def inner2():
        print("In inner2 function")

    return inner1, inner2


# Type 1
n1,n2 = outer()
n1()
n2()

# Type 2
retVal = outer()
# Single return val is -> object and multiple is -> tuple
retVal()            # TypeError: 'tuple' object is not callable

# print(retVal, type(retVal))
retVal[0]()
retVal[1]()

# Type 3
for i in retVal:
    i()

        