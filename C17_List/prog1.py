# List creation done by 3 ways -> list literals, list constructor, list comprehension


'''# 1. List Literals'''


data = [1,2,3,4]
print(data)

batRun = ['rohit', 47, 'shubhman', 80, 'virat', 117, 'shreyas', 108, 397, 7.9]
print(type(batRun), batRun)

emp = [{11,'ram', 3.1}, {12, 'shyam', 4.3}, {'virat':18}, (4,5,6)]
print(type(emp), emp, type(emp[2]))


'''# 2. List Constructor'''


player = list()             # list((12,23,4,5))      list({8:'jaddu'})     
print(type(player), player)

# list(4)           -->         TypeError: 'int' object is not iterable

# listD = [12,23,34]

# listD = {{12:23},{34:56}}               # TypeError: unhashable type: 'dict' --> it is due to outer {} -> set performs hashing to internally to store values and it's element is in form of k:v pairs which is not hashable

# listD = {{3,4,5,6}}                   # TypeError: unhashable type: 'set'

listD = [{12:23},{34:56}]               # It works because list does not used hashtable like concept internally

nList = list(listD)

print(nList)


'''# 3. List Comprehension'''


normList = [n for n in range(1,11)]

print(normList, type(normList))

evenSqrList = [num*num for num in range(1,11) if num%2==0]          # This syntax can be possible due to parser

print(evenSqrList)

