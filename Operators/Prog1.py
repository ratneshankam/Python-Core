# Unary Operator

x = 10
x = True
print(x)

a = -x
print(a)

a = +x
print(a)

a = ++x                     # pre increment operator --> gives same value (10)
print(a)

# a = x++                     # post increment operator --> SyntaxError: invalid syntax
print(a)

y = 20

a = ++x +++++ y                  # 30 -> any multiple + operator ignores with x + (++++y) internally
print(a)