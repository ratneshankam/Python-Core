"""
def fun(z, x, y):
    pass

fun(x=10, p=20, z=30)           # TypeError: fun() got an unexpected keyword argument 'p'

def fun2(**argc, x, z):
    pass


fun2(x=10, p=20, z=30)           # SyntaxError: arguments cannot follow var-keyword argument         
"""

def fun3(x, z, **argc):
    print(x,z,argc)                 # 10 30 {'p': 20}

fun3(x=10, p=20, z=30)


# NOTE: It is recommended that if you are using keyword args [**argc] then do not give other parameter

