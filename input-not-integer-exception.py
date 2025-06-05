#Raise an exception when input is not a number

try:
    x = int(input("Enter Integer: "))
    print(x)
except ValueError:
    print("Enter Value is not an Integer")