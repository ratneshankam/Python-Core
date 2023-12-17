playerList = ['Rohit', 'Virat', 'MSD']
# pName = str(input("Enter player name:"))
pName = (input("Enter player name:"))

for player in playerList:
    if (pName == player.lower()):
        print(f'{player} is present in the list')
        break
# This is called else suite for looping statement
else:                                           
    print(f'{pName} is not present in this list -> {playerList}')