x = 1
for i in range(3):
    for j in range(3):
        print(x, end=" ")
        x+=1
    # x+=1
    print()
    
'''
o/p: 
* If x+=1 is in inner loop
1 2 3 
4 5 6
7 8 9

* If x+=1 is in outer loop
1 1 1 
2 2 2
3 3 3
'''    