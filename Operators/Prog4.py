# Logical Operator --> {Logical AND (and), Logical OR (or), Logical NOT (not)}


# Logical Operator with boolean values
a = True
b = True

print(a and b)
print(a or b) 
print(not b)  

print(bool(b))

print(type(b))

print(id(a))

print(id(b))


# Logical Operator with Numeric values
a = 0               # Try variation with values 0,1,-1
b = 0               # # Try variation with values 0,1,-1

# numerical values greater than 0 are represent true
print(a and b)          # In and -> both should be true to Return True; hence it will Return second value (20 in this case)
print(a or b)           # In or -> only one is required to be true to Return True; hence it will Return first value (10 in this case)
print(not b)            # Not 20 (True value) --> False

print(bool(b))

print(type(b))

print(id(a))

print(id(b))
