# Passing variable number of keyword args

def fun(**argc):
    print(type(argc))           # <class 'dict'>
    print(argc)             # Directly prints dictionary
    
    # Print dict values using for loop
    for key, value in argc.items():
        print(key, ":", value)
    
fun(x=10, y=20, z=30)