#raise an exception when input i not a number

try:
    x=int(input("enter integer:"))
    print(x)
except ValueError:
    print("enter value is not a integer")
    