a = input("Enter the value: ")                  # By default return type of input() function is <class 'str'>
b = input("Enter the value: ")

print(a+b)              # It will concat input str a and b

# It is also possible
a = str(input("Enter the value: "))
b = str(input("Enter the value: "))

print(a+b)

# Real Time example of Input data

print("Moive Data: ")

mName = input("Enter movie name: ")
mCollection = float(input("Enter gross collection: "))
mTickets = int(input("Enter No. of tickets: "))

print("Movie Data:", mName, "Movie Collection:", mCollection, "No. of tickets:", mTickets)

