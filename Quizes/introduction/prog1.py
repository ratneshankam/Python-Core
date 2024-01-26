__str__ = 1
print(__str__)

import sys
# python interpreter name is 
print("python interpreter name is: ", sys.executable)

import array as arr
data = arr.array('i', [101,1,2,3])
print(data[1:10:])

import numpy
arr = numpy.array((2,3,4))
print(arr)