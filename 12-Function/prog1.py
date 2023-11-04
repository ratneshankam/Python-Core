# function body => also called 'Suite'

# Anywhere there is ':' u suppose to give body {if u don't want to do anything inside that simply write 'pass' keyword and return}
# For example -->
def fun(): pass
if True: pass

''''keyword funName call->'()' parameters : <-- prototype function definition '''
def sumTwo(a,b):
    print('In function')
    ans = a+b
    print(ans)
    
sumTwo(int(input('enter no:')), int(input('enter no:')))
