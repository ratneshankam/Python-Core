def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

result = multiply(2,3,4)
print(result)