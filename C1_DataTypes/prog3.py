"""
Sequence DataType:
1.String
2.List
3.Tuple
4.Range
"""

# String            --> Standard representation of string is 'str' in a single quote
s1 = "Hi"
s2 = 'Hey'
s3 = '''Hello'''
s4 = """Namaste"""

print(s1,s2,s3,s4)                  # Hi Hey Hello Namaste
print(type(s1))                     # <class 'str'>
print(type(s2))                     # <class 'str'>
print(type(s3))                     # <class 'str'>
print(type(s4))                     # <class 'str'>

# List
pData = [18,7,10,"virat",'sachin','''Mahi''', 45.5, 34.7, 56.8, 18,7,10]
print(pData)                       # Duplicate data allowed
print(type(pData))                 # <class 'list'>

pData[5] = 'msd'                    # list is mutable py recognise it with [] brakets
print(pData)

# Tuple
empTuple = ('c', "cpp", "java", "py")
print(empTuple)
# empTuple[2] = "ruby"                # TypeError: 'tuple' object does not support item assignment  --> That means tuple is immutable

# Range
x = range(10)
print(x)                            # range(0, 10)
print(type(x))                      # <class 'range'>

for i in x:
    print(i)

