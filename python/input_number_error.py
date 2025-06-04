try:
    a=int(input("enter  a number:"))
    result=a+5
except ValueError as e:
    print("not a number")
else:
    print("value is:",result)