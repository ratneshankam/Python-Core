# It's an example of why python is interpreted language.
def fun():
    print("In function")

class Demo:
    fun()
    print("Start class")

    def __init__(self):
        print("In constructor")

    print("End class")

print("Start code")
# obj = Demo()                # try with commenting obj
print("End code")
