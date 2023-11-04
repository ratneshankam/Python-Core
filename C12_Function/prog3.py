# Returning multiple values

def addByTen(x,y,z):
    return x+10, y+10, z+10

a = int(input())
b = int(input())
c = int(input())

# in parameter and assign variable xyz are different 
x,y,z = addByTen(a,b,c)
print(x,y,z)

# Can store in one variable also
retVal = addByTen(a,b,c)
print(retVal, type(retVal))

for i in retVal:
    # print(type(i))
    print(i)