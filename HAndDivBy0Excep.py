a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
try:
    print("Result:", a / b)
except ZeroDivisionError:
    print("Can't divide by zero!")
