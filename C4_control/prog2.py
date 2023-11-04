age = int(input("Enter your age: "))

if(age>18):
    pass                    # Used for empty body (condition true/false didn't affect)
print("Out of if")

# It shows that any value except 0 is True
x = 0
y = 12
z = -12

if (x):
    print(True)
elif (z):
    print("z is True")
elif (y):
    print("y is True") 
    
print(bool(x))
print(bool(y))
print(bool(z))