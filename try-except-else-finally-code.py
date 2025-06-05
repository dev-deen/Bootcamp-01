#Write a function with try-except-else-finally blocks

try:
    a = int(input("Enter first number to divide: "))
    b = int(input("Enter second number to divide: "))
    c = a/b
except ZeroDivisionError:
    print("Division cannot be performed by zero")
except ValueError:
    print("Value is not an Integer")
else:
    print(c)
finally:
    print("Code Execution Successfull")