# parameterized decorator function

def decorFun(func):
    print("In decor fun")

    # def wrapper(**kwargs, *args):             # SyntaxError: arguments cannot follow var-keyword argument
    def wrapper(*args, **kwargs):
        print("Start wrapper")
        
        func(*args, **kwargs)
        
        sumD=0
        for i in args:
            sumD += i
        for k,v in kwargs.items():
            sumD += v
        print("End wrapper")
        return sumD
        
    return wrapper

@decorFun
def normalFun(w,z,x,y):
    print("In normalFun")
    return x+y
    # return x+y+w+z

# normalFun = decorFun(normalFun(1,2))
# print(normalFun)

# normalFun()         # TypeError: 'int' object is not callable

# normalFun = decorFun(normalFun)
print(normalFun(1,2,y=10,x=20))