# Decorator Chaining

def decorFun(func):
    print("In decor fun")

    def wrapper():
        print("Start wrapper2")
        func()
        print("End wrapper2")
        
    return wrapper

def decorRun(func):
    print("In decor run")

    def wrapper():
        print("Start wrapper1")
        func()
        print("End wrapper1")
        
    return wrapper

# @decorFun
# @decorRun
def normalFun():
    print("In normalFun")
    
# normalFun = decorFun(decorRun(normalFun))
normalFun()