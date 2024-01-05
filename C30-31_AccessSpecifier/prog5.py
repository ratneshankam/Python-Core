class Demo:
    def __init__(self):
        print("In constructor")
    def __fun(self):
        print("In private function")

print(dir(Demo))                            # class Namespace

obj = Demo()
# obj.__fun()                                 # AttributeError: 'Demo' object has no attribute '__fun'
obj._Demo__fun()

print(dir(obj))
'''
__fun() method is instance method and still showing in class namespace -> it's just a placeholder not actually got memory in class namespace i.e error for below line
'''
# Demo._Demo__fun()         # error