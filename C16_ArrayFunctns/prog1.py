# Different ways to import libraries

import array as arr

jerNo = arr.array('i', [1,2,3])

print(type(jerNo))                              # <class 'array.array'>

import array

# jerNo = array('i', [1,2,3])                   # TypeError: 'module' object is not callable. Did you mean: 'array.array(...)'?

jerNo = array.array('i', [1,2,3])

from array import *

# jerNo = array.array('i', [1,2,3])             # AttributeError: type object 'array.array' has no attribute 'array'

# jerNo = array('x', [])                        # ValueError: bad typecode (must be b, B, u, h, H, i, I, l, L, q, Q, f or d)

jerNo = array('b', [12,34,56,127,-128])   

# If -129 added to array -> OverflowError: signed char is less than minimum
# If 128 added to array -> OverflowError: signed char is greater than maximum    

print(jerNo)

jerNo = array('q', [12,34,56,127,128, 255])   

print(jerNo, jerNo.itemsize)

jerNo = array('u', ['r', 'o', 'h', 'i', 't'])

# jerNo = array('u', ['rohit', 'klrahul', 'virat'])       # TypeError: array item must be unicode character

print(type(jerNo))                              # <class 'array.array'>

print(jerNo)                                    # array('u', 'rohit')

print(jerNo.itemsize, jerNo.typecode)           # itemsize: it will display typecode size like 'i'-> 4, 'd'-> 8 and typecode: returns the initialized array typecode

for i in jerNo:
    print(i)
    
'''
# Through Python prompt - help()

     |      Type code   C Type             Minimum size in bytes
     |      'b'         signed integer     1
     |      'B'         unsigned integer   1
     |      'u'         Unicode character  2 (see note)     
     |      'h'         signed integer     2
     |      'H'         unsigned integer   2
     |      'i'         signed integer     2
     |      'I'         unsigned integer   2
     |      'l'         signed integer     4
     |      'L'         unsigned integer   4
     |      'q'         signed integer     8 (see note)     
     |      'Q'         unsigned integer   8 (see note)     
     |      'f'         floating point     4
     |      'd'         floating point     8
     |
     |  NOTE: The 'u' typecode corresponds to Python's unicode character. On
     |  narrow builds this is 2-bytes on wide builds this is 4-bytes.
     |
     |  NOTE: The 'q' and 'Q' type codes are only available if the platform
     |  C compiler used to build Python supports 'long long', or, on Windows,
     |  '__int64'.
'''
