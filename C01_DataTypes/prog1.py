"""
Numeric DataType:
-> int
-> float
-> complex number
"""
empId = 20
print(empId)                        # 20
print(type(empId))                  # <class 'int'>

empSal = 2.2
data = 45.77777776666664444333
print(empSal)                        # 2.2
print(data)                          # 45.777777766666645   <-- It takes 15 digits after decimal point
print(type(empSal))                  # <class 'float'>

# Complex number type contains [a+bi] format where a is real and b is imaginary part and i is suffix
complexNum = 1+2.2j
print(complexNum)                        # (1+2.2j)
print(type(complexNum))                  # <class 'complex'>
