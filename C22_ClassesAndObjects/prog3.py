# The function binded in class called -> method
# Even class object not created print statements/ static/class variable executes
class Company():
    print('Incubator')
    def __init__(self):
        print('In constructor')
        
    def course(self):
        print('In python')
    print(course, id(course))
    course(1)

    def course():
        print('In course1')
    course()
    print(course, id(course))
    
    def course(x):
        print('In course2')
    # course()
    course(1)
    print(course, id(course))
    
    

obj = Company()
obj.course()          # TypeError when course(self) method not written
# course()              # NameError
# print(course, id(course))     # NameError

print(obj.course, id(obj.course))


def course():
        print('In course1')
course()
print(course, id(course))

def course():
        print('In course1')
course()
print(course, id(course))

def course(x):
    print('In course2')

# course()
course(1)
print(course, id(course))

def course(x):
    print('In course2')

# course()
course(1)
print(course, id(course))

# For example
a = 10
print(a, id(a))
x = 10
print(x, id(x))
a = 20
print(a, id(a))

'''
O/P:
Incubator
<function Company.course at 0x0000022751E5E200> 2367901000192
In python
In course1
<function Company.course at 0x0000022751E5E340> 2367901000512
In course2
<function Company.course at 0x0000022751E5E200> 2367901000192
In constructor
In course2
<bound method Company.course of <__main__.Company object at 0x0000022751E70FE0>> 2367901102016
In course1
<function course at 0x0000022751C88A40> 2367899077184
In course1
<function course at 0x0000022751E5E340> 2367901000512
In course2
<function course at 0x0000022751C88A40> 2367899077184
In course2
<function course at 0x0000022751E5E340> 2367901000512
10 140720074836696
10 140720074836696
20 140720074837016
'''