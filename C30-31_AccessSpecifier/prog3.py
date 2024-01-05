class Demo:
    def __init__(self):
        print("In constructor")
    def __del__(self):
        print("In destructor")


def fun():
    print("In fun")
    obj = Demo()
    print("End fun")
    
    
fun()                       # check the fun block after it's execution get's completed destructor called

def gun():
    print("In gun")
    obj = Demo()
    print("End gun")
    return obj
    
obj = gun()
print("End code")