# Different ways for Output print() types

# Type 1

x = 10
y = 20

print(x)
print()                         # prints a blank line and then ENTER(\n)
print(y)

# Type 2

print('c2w' + 'Incubator')              # c2wIncubator
print('c2w' , 'Incubator')              # c2w Incubator
print(3*'incubator')                    # incubatorincubatorincubator

# Type 3

print(x,y)                              # It means default {sep = " "} is this 
print(x,y,sep=":")
print(x,y,sep=",")

print(x,y, end = " ")
print("Hello")

# Type 4

print("Value of x = %d" % x)                # Even %i is also works
print("Value of x = %f" % y)

print("value of x: {} and y: {}".format(x,y))

print(f"value of x: {x} and y: {y}.")
