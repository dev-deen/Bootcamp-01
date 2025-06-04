try:
    a=int(input("enter number:"))
    b=int(input("enter number:"))
    print("result:",a/b)
except(ValueError,ZeroDivisionError) as e:
    print("errors found:",e)