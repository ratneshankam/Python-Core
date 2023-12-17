# int to str convert using chr()
x = 65
n = int(input("Enter no:"))
for i in range(n):
    for j in range(i+1):
        print(chr(x), end=" ")
        x+=1
    print()
    
    
print(type(chr(x)))


print(3,4)                          # By looking at python promt, --> in print() by default {[ sep=" " and end="\n" ]}

