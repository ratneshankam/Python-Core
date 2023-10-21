age = int(input("Enter your age: "))

if(age>18):
    print("Eligible for voting")
print("Out of if")


if(age>18):
print("Eligible for voting")            # IndentationError: expected an indented block after 'if' statement on line 8
print("Out of if")


# But this works!
if(age>18):
    
            print("Eligible for voting")
print("Out of if")


if (age<23)                             # SyntaxError: expected ':'
    print("age is less than 23")