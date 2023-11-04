def Outer(x,y):
    def Inner(a,b):
        print("In inner function")
        return a+b
    print("In outer fun")
    print(x+y)
    return Inner

retval = Outer(2,3)
# print(retval())                 # TypeError: Outer.<locals>.Inner() missing 2 required positional arguments: 'a' and 'b'

inretval = retval(4,3)          # inner call done and returning store into variable but didn't print it

print(retval)               # By simply printing return Obj addr -->  <function Outer.<locals>.Inner at 0x000001D64865D260>
