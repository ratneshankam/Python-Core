# Passing number of variable argument to function
# argc => no of argument count,  argv = no of variable argument     --> Standard Naming

def fun(*argc):                     # -> is a positional argument
    print(type(argc))                   # *argc --> TypeError: type() takes 1 or 3 arguments
    
    for i in argc:
        print(i, end=" ")
    print()

fun(10,20,30,40)