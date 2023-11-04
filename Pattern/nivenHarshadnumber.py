x = 5
count = 0
# for i in range(1, (x*x)+1):
for i in range(1, 100000):
    sum = 0
    num = i

    while(num != 0):
        sum += num%10
        num //= 10

    if (i%sum == 0):
        count += 1
        print(i, end=" ")
        
        if (count%5 == 0):
            print('_')
        
    if (count == (x*x)):
        break