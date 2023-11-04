# def fun(2,3): pass          # function parameter can't be const values

def fun(fact):
    factorial = 1
    for i in range(1,fact+1):
        factorial *= i

    return factorial

print(fun(4))