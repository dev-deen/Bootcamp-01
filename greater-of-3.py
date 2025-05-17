#Find the largest of three numbers
x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
z = int(input("Enter 3rd number: "))
if (x > y) and (x > z):
    print("1st number ", x, "is greater")
elif (y > x) and (y > z):
    print("2nd number ", y, "is greater")
else:
    print("3rd number ", z, "is greater")