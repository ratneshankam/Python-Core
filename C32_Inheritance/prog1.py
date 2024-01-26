class Parent1:
    def __init__(self):
        print('parent1')
        
class Parent2:
    def __init__(self):
        print('parent2')
        
class Child(Parent1, Parent2):
    pass
    # def __init__(self):
    #     print('child')
        
obj = Child()
print(Child.mro())