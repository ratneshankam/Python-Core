x = ('Today')
print(type(x))
print(x)

y = (2,3,2)
print(type(y))
print(y)


z = -234.4
print(z)

"""
x = None
x = 5  # This is fine, it changes the reference of x to a different object (integer 5)
x = None  # This is also fine, it changes the reference back to the None object
x = x + 1  # This would throw an error, as you can't modify None
"""

a = 10
b = None
print(a==b)

a = True
b = False
print(a+b)

sampleset = {'Yellow', 'Orange', 'Black'}
print(sampleset)


a = 3
b = 1

a,b = b,a                       # To swap 2 numbers
print(a,b)

print(type(a) == type(b))

###############################################
a = 2
b = 3

c = 5 + 4j + a*b

print(c)