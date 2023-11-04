# Named Argument

def compInfo(compName, empCount):
    print(compName, empCount)

compInfo('Microsoft', 70000)
compInfo(10000, 'Google')


# To let not depend on position try named argument
compInfo(empCount=10000, compName='Google')