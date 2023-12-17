str1 = 'core2web'   
'''
# SyntaxError: unterminated string literal (detected at line 2)
str1 = "Incubator
"
'''

s = 'welcome to "python"'
print(s)
s = "welcome to 'python'"
print(s)

# Escape sequence character
s = "Welcome to\tCore2web \n Pune"
print(s)
s = r"Welcome to\tCore2web \n Pune"     # r -> get's raw string
print(s)

# Unicode Format
s = "\u0906 \u0908"
print(s)

str = 'Core2web'
print(str[2], str[-5], str[0])
print(str[::2], str[2:5:], str[-2:-5:-1], str[-3::-1], str[2:5:-1])

print(str == str1)
print(str < str1)       # internal ascii value compare
print(str != str1)