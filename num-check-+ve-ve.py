#Check if a number is positive, negative, or zero
x = int(input("Enter number to check: "))
if x > 0:
    print(x, " is Positive")
elif x < 0:
    print(x, " is Negative")
elif x == 0:
    print(x, " is Zero")
else:
    print("Non - Numerical character entered, Please RE-Enter ur number correctly")