# Access specifiers
# In python everything is public to create private/protected variable is uses name mangling concept

class Demo:
    z=30                        # class/static variable
    def __init__(self):
        self._x = 10                            # protected variable
        self.__y = 20                           # _Demo__y  --> name mangling for private variable
        
print(dir(Demo))
obj = Demo()
print(obj._x)
# print(obj.__y)                                  # AttributeError: 'Demo' object has no attribute '__y'
print(obj._Demo__y)
print(Demo.z)

print(dir(obj), '\n')

print(Demo.__dict__)
print(obj.__dict__)