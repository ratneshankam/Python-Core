player = ['rohit', 'shubhman', 'virat', 'shreyas', 'KLrahul']
print(player)

p2 = player.copy()
print(p2)

player.append('jaddu')

player.extend(('surya', 'ishan'))               # extend --> takes iterable object as a input

player.insert(1, 'rohit')
print(player)

print(player.count('rohit'))

print(player.index('shreyas'))

player.reverse()            # It reverses original list didn't give copy
print(player)

player.sort()               # original list will be sort
print(player)

player.remove('rohit')      #1st occurance of element will be removed 

player.pop()                # by default pop will be removed list indexed element

player.pop(4)
print(player)

player.clear()
print(player)