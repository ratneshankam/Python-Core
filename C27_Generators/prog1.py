def fun():
    x = 10
    return x
    # Other prog languages gives error but not in python
    # After return statement -> exist code is unreachable
    x += 1
    return x

obj = fun()
print(obj)

print(fun())