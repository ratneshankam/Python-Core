x = int(input("Enter value of x:"))

if(x>20):
    print("x is greater than 20")
else:
        print("x is not greater than 20")
    print(x,"is x")                         # IndentationError: unindent does not match any outer indentation level 


if(x>20) {          # SyntaxError: invalid syntax
    print("Greater")
} else {
    print("Lesser")
}


# This way curly braces {} works!
if(x>20):
    print("x is greater than 20")
else:
    print("x is not greater than 20")
    {
        print(x,"is x")         
    }
    