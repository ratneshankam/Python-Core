# Assert -> keyword

name = input("Enter your name:")
age = int(input("Enter your age:"))

assert age>0, "Age negative not allowed"

if (age>18):
    print(name,"eligible for voting")
else:
    print(name,"not eligible for voting")