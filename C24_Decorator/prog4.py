# Function Decorator

def decorFun(func):
    print('In decorFun')

    def wrapper():
        print("Start wrapper")
        func()
        print("End wrapper")
    print(id(wrapper))
    
    # def w():
    #     print("In w")
    return wrapper

@decorFun
def normalFun():
    print("Hello, In normal fun")
    
# ret = decorFun(normalFun)
# ret()
# print(id(ret), type(ret))

# normalFun = decorFun(normalFun)
normalFun()
print(id(normalFun), type(normalFun))

# Multiple object return also works
# normalFun[0]()
# normalFun[1]()