#Handle division by zero exception

try:
    x = int(input("Enter number 1 : "))
    y = int(input("Enter number 2 : "))
    operation = x / y
    if x != 0 and y != 0:
        print(operation)
except ZeroDivisionError:
    print("Some Error Occured")
        