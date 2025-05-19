a=float(input("enter first number: "))
b=float(input("enter second number: "))
c=float(input("enter third number: "))
if a>=b and a>=c:
    print(",a is largest:",a)
elif b>=a and b>=c:
    print("b is largest:",b)
else:
    print("c is largest:",c)
