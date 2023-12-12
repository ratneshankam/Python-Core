from array import *

arrD = array('i', [1,2,3,4,5])

for i in arrD:
    print(i, end=" ")
print() 

print(arrD[4])
print(arrD[::])
print(arrD[1:2:-1])
print(arrD[2::-1])
print(arrD[2::2])

'''
OUTPUT:
1 2 3 4 5 
5
array('i', [1, 2, 3, 4, 5])
array('i')
array('i', [3, 2, 1])
array('i', [3, 5])
'''