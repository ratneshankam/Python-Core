playerList = ['Rohit', 'Virat', 'MSD']
# pName = str(input("Enter player name:"))
pName = (input("Enter player name:"))

for player in playerList:
    if (pName == player.lower()):
        print(f'{player} is present in the list')
        break                   #breaks the loop as we don't need to find further once it match

    elif player == playerList[-1]:
        print(f'{pName} is not present in this list -> {playerList}')