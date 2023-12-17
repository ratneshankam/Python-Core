class Company(object):
    def disp():
       print("hello")
    disp()
    print(disp, id(disp))

    def disp(self):
        print('self disp')
    print(disp, id(disp))

def fun():
    print('fun')


print('Start code')
# disp()            # NameError
Company().disp()
fun()

# In python everything is object and having unique value
print(type(Company))
print(type(fun))
print(type(print))

print('End code')


