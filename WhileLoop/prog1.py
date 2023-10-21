i = 1
j = i
while (i<5):
    print(i)
    # print(j)      j+=1
    i = i+1                 # comment this line 
    
# If we did not incre/decre value loop in into infinity but did not throw stack overflow exception due it stack is push/pop simultaneously in every instruction execution


print(i)            # 5



# Prints nums which are divisible by 5

i = 1
x = int(input())

while(i<=x):
    if(i%5==0):
        print(i)
    i += 1