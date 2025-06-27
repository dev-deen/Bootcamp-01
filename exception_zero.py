#Handling division by zero exception

try:
    x=int(input("enter first number:"))
    y=int(input("enter second number "))
    operation=x/y
    if x!=0 and y!=0:
        print(operation)
    except ZeroDivisionError:
print("some error occured")
