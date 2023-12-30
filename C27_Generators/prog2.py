def fun():
    print("start")
    yield 10
    print("mid")
    yield 20
    yield 30
    print("End")
    yield

retV = fun()    
print(retV, type(retV))

# print(next(retV))
# print(next(retV))
# print(next(retV))

# To remove this error we can add empty yield
# print(next(retV))           # Traceback (most recent call last):  StopIteration

for i in retV:     #fun()
    print(i)


# for i in range(10):
#     i=5
#     print(i)
#     i=5
