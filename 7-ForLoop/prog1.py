# Prints x in range of 1 (inclusive) and upto 5 (exclusive)
for x in range(1,5):
    print(x)
# O/p: 1,2,3,4


# Trying to reverse
for x in range(10,5):
    print(x)
# O/p: Prints nothing


# To actually reverse range add 3 parameter   -->   range(start, stop, step)

# Check the description of help(range) in python prompt


for x in range(1,15,3):
    print(x, end=" ")
    
# O/p: 1 4 7 10 13

for x in range(10,3,-2):
    print(x, end=" ")
    
    
# In for loop variable is indicates global scope -->

for i in range(1,5):
    print(i)
    
    
print(i)        # Generally we thinks it's a error, but in python i is global scope

# O/p:  1 2 3 4 4(i is 4 and exits loop)
# It's not 5 because range is goes from 1 to 4 only 5 is excluded