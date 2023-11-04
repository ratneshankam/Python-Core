# Default Parameter

def add(x, y=20):
    print(x,y)

add(20)
add(1,2)

# python is compiled and interpreted language because it print's output line by line 
# And called compiled because if it having syntactical error it directly gives error like indentation [It's not same about logical error]

    # add()           #IndentationError: unexpected indent [Even pylance extention recognizes this]
add()               # TypeError: add() missing 1 required positional argument: 'x'

