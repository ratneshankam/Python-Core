s = "Hello WORLD"
# 1.
print(s.capitalize())

# 2.
print(s.casefold())

# 3.
print(s.center(40, '#'))
print(s.center(4, '#'))

# 4.
print(s.count('o'))
print(s.count(s))

# 5.
print(s.encode('utf-16'))       # b'\xff\xfeH\x00e\x00l\x00l\x00o\x00 \x00W\x00O\x00R\x00L\x00D\x00' --> where b represents byte

print(b'Hello WORLD' == s)
print(r'Hello WORLD' == s)

# 6.
print(s.endswith('LD', 3, 18))

# 7.
extab = 'hi\tram'
print(extab, extab.expandtabs(tabsize=16))

# 8.
print(s.find('lo'))
print(s.find('world'))              # -1 on failure

# 9.
print("This string is {} ".format(s, extab))         # IndexError -> If positional args < compare to {} braces else it's fine

# 10.
print("This string is ".format_map(s))

# 11.
print(s.index('lo'))
# print(s.index('world'))           # valueError --> on failure

# 12.
st = 'virat18'
print(st.isalnum())

# 13.
st = 'virat'
print(st.isalpha())         # Even space is there in str -> returns False

# 14.
print(s.isascii)            # <built-in method isascii of str object at 0x0000022093A49AF0>  --> Gives address as everything in python is object
print(s.isascii())

# 15.
# st = '⅕18⁵'
st = '18'
st1 = '\u00BD'
c = '\u00B2'
print(st1, c)
print(st.isdecimal(), st1.isdecimal(), c.isdecimal())

# 16.
print(st.isdigit(), st1.isdigit(), c.isdigit())     # subscripts, superscripts are allowed

# 17.
print(st.isnumeric(), st1.isnumeric(), c.isnumeric(), 'Ⅺ'.isnumeric(), 'XI'.isnumeric())

# 18.
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"
print(a.isidentifier(),b.isidentifier(),c.isidentifier(),d.isidentifier())

# 19.           26.
print(s.lower(), s.islower())

# 20.
print('Hello!\nAre you #1?'.isprintable(), b.isprintable())

# 21.
print(' '.isspace(), s.isspace())

# 22.
print(s.title(), s.istitle())

# 23.
print(s.upper(), s.isupper())

# 24.
print('_'.join('hello'))        # join -> takes iterable as input
# print('.'.join([18,45,7,8]))    # TypeError: sequence item 0: expected str instance, int found
print('.'.join(['18','45','7','8']))

# 25.
print(s.ljust(40, '#'))

# 26.
print(s.lower())

# 27.
st = '  hi  '
print(st.lstrip())      # left whitespaces removed/stripped

# 28.
print(s.partition('lo'))
print(s.partition('hello'))
print(s.rpartition('hello'))

# 29.
st = 'welcome to wel-build'
print(st.removeprefix('wel'))       # If staring suffix exists then only remove else return string

# 30.
print(st.removesuffix('wel'))       # If staring suffix exists then only remove else return string

# 31.
print(st.replace('wel', 'self', 1))     # default count is -1 -> means replace all string

# 32.
print(st.rfind('wel'))

# 33.
print(st.rindex('wel'))

# 34.
print(st.rjust(40, "#"))

# 35.
print(s.rpartition('hello'))

# 36.
print(st.rsplit('l'))

# 37.
st1 = "  hi  "
print(st1.rstrip())

# 38.
print(st.split())

# 39.
st1 = "hey!\nhello\tpune\n"
print(st1.splitlines(), st1.splitlines(True))

# 40.
print(s.startswith('Hel'))

# 41.
st1 = "  hi  "
print(st1.strip())          # leading and trailing whitespace removed.

# 42.
print(s.swapcase())

# 43.
print(s.title())

# 44.
print(s.translate({'H':None, 'H':'l', 108:65, 76:97}))  # Only ascii value conversion

# 45.
print(s.translate(s.maketrans('H','T', 'l')))       # maketrans -> return a translation table usable for str.translate().
print(s.translate(s.maketrans('H','T',)))           # Even ',' extra typed at the end (not front) python didn't give error
print(s.translate(s.maketrans({'H':'T', 108:65, 76:97})))

# 46.
print(s.upper())

# 47.
print(s.zfill(15))      # with 0 filling at left

# 48.
print((str.mro()))            # method resolution order (MRO)->The MRO defines the order in which base classes are searched when looking for a method in a class hierarchy
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

# Using the .mro() method
mro_result = D.mro()

# Printing the result
print("Method Resolution Order:", mro_result)