x = 3
for i in range(x):
    for j in range(i+1):
        print(j+1, end=" ")
    print()


'''
# Nested-looping patterns can be printed like this in single loop

for i in range(1, x*x+1):
    print(i, end=" ")
    if (i%x == 0):
        print()
    '''