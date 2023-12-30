def fun(x,y):
    print('start')
    while(x<=y):
        yield x
        x+=1
    print('end')
    
retV = fun(1,10)
print(next(retV))

for val in fun(1,10):           # retV
    print("val", val)