# <class 'tuple'> 

t = ()
print(t, type(t))

lang = ('java', 'cpp', 'python', ('go', 'rust', 'dart'))

print(lang, type(lang))

print(lang[3][1])

lang[2] = 'ruby'        # TypeError: 'tuple' object does not support item assignment


'''
    tuple:
        collection of multiple object
        having indexing
        nested tuple is possible
        *tuple is immutable (i.e it doest not having methods like in dict/list)
'''