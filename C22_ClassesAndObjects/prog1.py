class Employee:         # Employee() -> also works
    print("In class")

    def __new__(cls):               # memory allocator
        print("creator")

        # If we don't return object instance of new it will never get called --> constructor
        print(cls)
        print(object.__new__(cls), '''super().__new__(cls)''')       # Here super() call shows different address
        print(super().__new__(cls))

        # Can be return as super(). too! If parenthesis is not given got -> TypeError
        return object.__new__(cls)
    
    def __init__(self):
        print("In constructor")     # It only get's called when obj is created
        print(self)
        
# print(Employee, Employee())
# Employee()

# If we do not write __new__ or __init__ compiler called it implicitly
# But usually to initialize instance variable we need __init__

obj = Employee
print(obj)
print(obj())



