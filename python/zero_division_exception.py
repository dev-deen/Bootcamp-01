try:
    num=int(input("enter numerator:"))
    denom=int(input("enter denominator:"))
    result=num/denom
except ZeroDivisionError as e :
    print("cannot divide by zero...!")
else:
    print("result:",result)

    