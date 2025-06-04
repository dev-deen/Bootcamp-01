try:
    a=int(input("enter first number:"))
    b=int(input("enter second number:"))
    result=a/b
except ZeroDivisionError as e:
    print("cannot divide by zero")
else:
    print("division successfull:",result)
finally:
    print("operation completed...!")