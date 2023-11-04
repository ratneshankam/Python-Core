def add(x=50, y, z=30):                 # SyntaxError: parameter without a default follows parameter with a default  [--> error means that default values should from right to left]
    print(x,y,z)
    
add(10,20)