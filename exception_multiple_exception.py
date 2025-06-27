#handling multiple exception in one block

try:
    l=[1,2,3]
    a=int(input("enter index value from list to divide:"))
    b=int(input("enter number to divide:"))
    div=l[a]/b
    print(div)
except IndexError:
    print("index value does not exist")
except ZeroDivisionError:
    print("Division by zro is not acceptable")
