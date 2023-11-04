def fun(*argv, x, y):               # TypeError: fun() missing 2 required keyword-only arguments: 'x' and 'y'
    
# def fun(x, y, *argv):
    print(type(*argv))
    print(x, y, *argv)
    
fun(10, 20, 30)
fun(10, 20)