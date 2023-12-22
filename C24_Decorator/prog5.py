def fun(x, y):
    return x+y

def run(*args):
    sumD = 0
    print(type(args))
    for i in args:
        sumD += i
    return sumD

print(run(1,2,3,4))
print(fun(3,4))

print(run())
# print(fun())          # TypeError

# print(run(x=1,y=4))         # TypeError: run() got an unexpected keyword argument 'x'

def fun(x, y):
    return x+y

def run(**kwargs):
    sumD = 0
    print(type(kwargs))
    for k,v in kwargs.items():
        sumD += v
    return sumD

print(fun(y=1,x=4))

# print(run(1,2,3,4))             # TypeError: run() takes 0 positional arguments but 4 were given

print(run(y=1,x=4,z=5))
