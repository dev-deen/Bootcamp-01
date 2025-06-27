# function with try-except-else-finally blocks

try:
    a=int(input("enter first number :"))
    b=int(input("enter the second number:"))
    c=a/b
except ZeroDivisionError:
    print("division can not be performed by zero")
except ValueError:
    print("value is not a integer")
else:
    print(c)
finally:
    print("code execution successfull")
    
