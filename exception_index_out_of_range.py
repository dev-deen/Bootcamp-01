# index out of range

try:
    i=[1,2,3]
    a=int(input("enter index of value that you wamt to print"))
    print(l[a])
except IndexError:
    print("index out of range")
    