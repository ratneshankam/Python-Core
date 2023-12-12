# shallowcopy and deepcopy concept and differences

lang = ['java', 'cpp', 'python']

data = lang.copy()

print(lang)
print(data)

lang[1] = 'c'

print(lang)
print(data)

# Nested list
lang = ['java', 'cpp', 'python', ['go', 'rust', 'dart']]

data = lang.copy()

print(lang)
print(data)

lang[1] = 'c'
lang[3][1] = 'javascript'           # Shallow copy only works for nested list [as it behaves like a dangling pointer in c] to avoid this ambiguity we can use deepcopy() function of copy module

print(lang)
print(data)

print('''**************************************************************************************''')

import copy as cp

lang = ['java', 'cpp', 'python', ['go', 'rust', 'dart']]
d = cp.deepcopy(lang)

print(lang)
print(d)

lang[1] = 'c'
lang[3][1] = 'javascript'

print(lang)
print(d)
