player = {45:'rohit', 77:'shubhman', 18:'virat', 96:{41:'shreyas', 1:'KLrahul'}}

# If key is already exist is will update it's value else if key not found it will add at the end
player[8] = 'jaddu'
player[18] = 'xyz'

print(player)

# --------------------Methods for accessing

print(player.get(45))

print(player.items())           # dict_items([(45, 'rohit'), (77, 'shubhman'), (18, 'xyz'), (96, 'shreyas'), (1, 'KLrahul'), (8, 'jaddu')])

# but mostly items() method used this way

for key,value in player.items():
    print(key, '=', value)

print(player.keys(), player.values())

# -------------------Methods for deleting

player.popitem()

# player.pop()            # TypeError: pop expected at least 1 argument, got 0 

player.pop(45)

# player.clear()

print(player)

# -------------------Some Other Methods

import copy as cp
newDeepCp = cp.deepcopy(player)

newD = player.copy()        # it will gives shallow copy (which will be only works in nested dict)

print(player)
print(newD, newDeepCp)

player[96][1] = 'shetty'

print(player)
print(newD, newDeepCp)

print('********************************************************************************')
newD = {18:'virat', 99:'ashwin'}

player.update(newD)     # It will append elements that not in newD and if key found update it's value
print(player, newD)

val = player.setdefault(18, 'yuvi')         # If key is already present it will return it's existing value in container else if key not found add at the end and return it's value
print(player, '\n', val)


lang = ['reactJs', 'flutter', 'springboot']

teacher = 'shashi'            # Always remember 'str' is iterable


nDict = player.fromkeys(lang, teacher)       # takes 2 parameter 1st is keys(in iterable obj format) and nother one is value(any format)
print(nDict)

# We do player.fromkeys because just to (just need dict object) access fromkeys() method which is in <class 'dict'> it didn't impact any on player

print(player)