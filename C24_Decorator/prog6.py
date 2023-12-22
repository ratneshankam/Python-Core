# parameterized decorator function

def decorFun(func):
    print("In decor fun")

    def wrapper(*args):
        print("Start wrapper")
        
        func(*args)
        
        sumD=0
        for i in args:
            sumD += i
        print("End wrapper")
        return sumD
        
    return wrapper

@decorFun
def normalFun(x,y):
    print("In normalFun")
    return x+y

# normalFun = decorFun(normalFun(1,2))
# print(normalFun)

# normalFun()         # TypeError: 'int' object is not callable

# normalFun = decorFun(normalFun)
print(normalFun(10,20))