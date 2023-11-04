# Function parameter
# [It works in version 3+ not in version 2]

# It actually comes to improve readability does not affect input
def fun(x:int, y:int):
    print(x,y)

fun(2,3)
fun('A','B')

def fun(a:int, b:int) -> int:
    print(a,b)
    return 'hello'

print(fun(3,4))