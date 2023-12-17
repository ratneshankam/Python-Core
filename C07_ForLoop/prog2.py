# Ques: Take 2 nums from input and print range in between

x = int(input())
y = int(input())

for i in range(x, y+1):         # Doing y+1 to including y also while printing
    print(i)
    
# Ques: Take 2 nums from input and print range in between

x = int(input())
y = int(input())

for i in range(x, y+1):
    if(i%2 == 0):
        print(i, "is even")
    else:
        print(i,"is odd")
        
        
# Ques: Take 2 nums from input and prints nums in range of which is divisible by 4 and 5

x = int(input())
y = int(input())

for i in range(x, y+1):         # Doing y+1 to including y also while printing
    if (i%4 == 0 and i%5 == 0):
        print(i)
        
        
