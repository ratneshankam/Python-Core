'''
Array module(library):                                      # Module can be said as having multiple functionality similar to class
    multiple elements/objects (collection)
    similar type
    index based and starts with 0
    can accessible using index & subscript
    jerNo[2] => 18
'''

import array as arr                                 # as arr -> is optional to call as it's name


'''
    Trial and Error:
         jerNo = array('i',[45,77,18,96,1])
            ^^^^^
        NameError: name 'array' is not defined.

        jerNo = arr.array([45,77,18,96,1])
            ^^^^^^^^^^^^^^^^^^^^^^^^^^
        TypeError: array() argument 1 must be a unicode character, not list

        jerNo = arr('i',[45,77,18,96,1])
            ^^^^^^^^^^^^^^^^^^^^^^^^
        TypeError: 'module' object is not callable.
'''

jerNo = arr.array('i',[45,77,18,96,1])

print(jerNo)                # array('i', [45, 77, 18, 96, 1])
print(type(jerNo))          # <class 'array.array'>

jerNo = arr.array('i',[])
print(jerNo)                    # array('i')
jerNo = arr.array('i')
print(jerNo)                    # array('i')


'''
    Array fields:
        jerNo --> array
        arr --> module
        array()  --> funtion (actually class) #read in help-prompt
        'i' --> is typecode(datatype)        
        [] = collection (iterable can say)
'''



jerNo = arr.array('i',[45,77,18,96,1])

for ele in jerNo:
    print(ele, end = "  ")    