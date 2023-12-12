'''
# Different imp functions

     |  Methods:
     |
     |  append() -- append a new item to the end of the array
     |  buffer_info() -- return information giving the current memory info
     |  byteswap() -- byteswap all the items of the array
     |  count() -- return number of occurrences of an object
     |  extend() -- extend array by appending multiple elements from an iterable
     |  fromfile() -- read items from a file object   
     |  fromlist() -- append items from the list      
     |  frombytes() -- append items from the string   
     |  index() -- return index of first occurrence of an object
     |  insert() -- insert a new item into the array at a provided position
     |  pop() -- remove and return item (default last)
     |  remove() -- remove first occurrence of an object
     |  reverse() -- reverse the order of the items in the array
     |  tofile() -- write all items to a file object  
     |  tolist() -- return the array converted to an ordinary list
     |  tobytes() -- return the array converted to a string
     |
     |  Attributes:
     |
     |  typecode -- the typecode character used to create the array
     |  itemsize -- the length in bytes of one array item
'''

from array import *

jerNo = array('i', [45,77,18,96,1])

jerNo.append(18)

print(jerNo.buffer_info())

jerNo.extend([12,10,7])         # TypeError: 'int' object is not iterable           --> That means it takes iterable type object as a input like list,tuple,dict

jerNo.extend({3:4,5:4})

jerNo.insert(5, 18)            # TypeError: insert expected 2 arguments, got 1

print(jerNo.count(18))          # returns the frequency of that element in the array

print(jerNo.index(18))           # 1st occurance element index position

jerNo.reverse()             # It reverses the original array didn't give copy

data = [8,99]

jerNo.fromlist(data)            # it will append the list to an original array

jerNoList = jerNo.tolist()

print(type(jerNoList), '\n', jerNoList)

jerNo.remove(18)

# jerNo.remove(2)               # ValueError: array.remove(x): x not in array

jerNo.pop()                 # by default removes last element in the array

jerNo.pop(4)

# jerNo.clear()            # AttributeError: 'array.array' object has no attribute 'clear'

print(jerNo)


