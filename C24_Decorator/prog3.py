# Code1
def run():
    print("In run")

def fun(x):
    x()
    print("In fun", type(x))
    
# fun(run)
print(type(fun(run)), type(run))

# Code2

def gun():
    print("In gun")

def run(y):
    y()
    print("In run")

def fun(x):
    x()
    print("In fun", type(x))
    
fun(run(gun))