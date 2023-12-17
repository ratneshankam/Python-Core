# prints 1 to 5 in while running for loop upto 10 without using break/continue/pass statement

x = 10
'''for i in range(1,x+1):          
    print(i)
    if (i>4):
        i = 12                  # here i changes but does not affect in looping statement as i is bind to the range()  --> *class(not fun check in prompt)
        print(i)
    '''

i=1
while(i<=x):
    print(i)
    if i==5:
        i = 11
    # Increment
    i+=1