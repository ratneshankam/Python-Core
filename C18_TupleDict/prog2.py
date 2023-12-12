player = {}                     # empty {} is type -> dict not the set

print(player, type(player))

# player = {45:'rohit', 18:'virat', 1:'klrahul'}

player = dict({45:'rohit', 18:'virat', 1:'klrahul'})            # Using dict() constructor

print(player)

# Mixed data

myInfo = {'name': 'shashi', 3: ['c2w', 'biencaps', 'incubator'], 'team': {1:'sachin', 2:'rahul', 3:'akshay'}}
print(myInfo)

# print(myInfo[1])            # keyerror: 1

# dictionary: --> does not having indexing can be access through key

print(myInfo[3][1])

print(myInfo['team'][2])

print('********************************************************************************')

