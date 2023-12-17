import sys
print(type(sys.argv), sys.argv)

'''
If while running program input is given like PS A:\> python prog1.py 1 2 3 4                          
then O/P: <class 'list'> ['prog1.py', '1', '2', '3', '4']
'''

for i in sys.argv:
    print(i, end=" ")
print()

size =len(sys.argv)
print(size)

add = 0
for i in range(1,size):
    add+=i
print(add)