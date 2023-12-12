# # Methods in set
# '''
#  |  add(...)
#  |      Add an element to a set.
#  |
#  |      This has no effect if the element is already present.
#  |
#  |  clear(...)
#  |      Remove all elements from this set.
#  |
#  |  copy(...)
#  |      Return a shallow copy of a set.
#  |
#  |  difference(...)
#  |      Return the difference of two or more sets as a new set.
#  |
#  |      (i.e. all elements that are in this set but not the others.)
#  |
#  |  difference_update(...)
#  |      Remove all elements of another set from this set.
#  |
#  |  discard(...)
#  |      Remove an element from a set if it is a member. |
#  |      Unlike set.remove(), the discard() method does not raise
#  |      an exception when an element is missing from the set.
#  |
#  |  intersection(...)
#  |      Return the intersection of two sets as a new set.
#  |
#  |      (i.e. all elements that are in both sets.)    
#  |
#  |  intersection_update(...)
#  |      Update a set with the intersection of itself and another.
#  |
#  |  isdisjoint(...)
#  |      Return True if two sets have a null intersection.
#  |
#  |  issubset(...)
#  |      Report whether another set contains this set. 
#  |
#  |  issuperset(...)
#  |      Report whether this set contains another set. 
#  |
#  |  pop(...)
#  |      Remove and return an arbitrary set element.   
#  |      Raises KeyError if the set is empty.
#  |
#  |  remove(...)
#  |      Remove an element from a set; it must be a member.
#  |
#  |      If the element is not a member, raise a KeyError.
#  |
#  |  symmetric_difference(...)
#  |      Return the symmetric difference of two sets as a new set.
#  |
#  |      (i.e. all elements that are in exactly one of the sets.)
#  |
#  |  symmetric_difference_update(...)
#  |      Update a set with the symmetric difference of itself and another.
#  |
#  |  union(...)
#  |      Return the union of sets as a new set.        
#  |
#  |      (i.e. all elements that are in either set.)   
#  |
#  |  update(...)
#  |      Update a set with the union of itself and others.
# '''

# s1 = {1,2,3,4}

# # s1.add(5)
# print(s1)

# newS = s1.copy()
# print(s1, newS)

# s2 = {3,4,5,6}
# s3 = s1-s2
# print(s3)

# s3 = s1.difference(s2)
# print(s3)

# # s3 = s1.difference_update(s2)
# print(s1, s2, s3)

# s1.discard(12)          # if non-existing value is given it didn't give any error
# print(s1)

# s3 = s1.intersection(s2)
# print(s1, s2, s3)

# # s1.intersection_update(s2)
# print(s1, s2)


# print(s1.isdisjoint(s2))
# print(s1.issubset(s2))
# print(s1.issuperset(s2))

# s3 = s1.symmetric_difference(s2)            # a-b U b-a
# print(s1, s2, s3)

# # s1.symmetric_difference_update(s2)
# print(s1, s2)

# s3 = s1.union(s2)            # a U b
# print(s1, s2, s3)

# # s1.update(s2)
# print(s1, s2)

# s1.pop()        # Hashtable is in stack form returning element in reverse order i.e from start element is popping
# print(s1)

# s1.remove(2)
# s1.remove(23)                   # KeyError: 23   --> error satisfies that set is internally dict
# # And it is the only difference between remove() and discard() method

# print(s1)


list1 = [1,3]
list2 = list1
list1[0] = 4
print(list1)
print(list2)