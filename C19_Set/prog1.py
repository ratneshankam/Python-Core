data = {12,12,12}
data = {1,2,3,4,5,6,30,31,32,33,34,35}      # Iternally it uses hashtable to store data

# data = {'A', 'B', 'C'}                # Every time gives different output

print(data)

d = {}
print(d, type(d))

s = set()
print(s, type(s))

s = {10.5,'A', True, False, 1, 0}         # Internally True -> 1 and False -> 0 and i.e set does not store duplicate values hence true and false not shown while printing set
s = {1, 0, 10.5,'A', True, False}
print(s)

# print(s[2])         # As set perform hashing to store values therefore sequence is not define
# ---> TypeError: 'set' object is not subscriptable

# s[2] = 50           # TypeError: 'set' object does not support item assignment             diff. error came because --> workflow is always from right to left for example (x = 10+20+30 i.e it's calculation first done and store in variable)

s.add(6)
print(s)

# To create immutable set we used frozenset

setD = frozenset([10,20,30,40])

# print(setD.add(4))          # AttributeError: 'frozenset' object has no attribute 'add'






