#Handle index out of range exception

try:
    l = [1,2,3,4,5]
    a = int(input("Enter Index of value u want to print: "))
    print(l[a])
except IndexError:
    print("Index is Out Of Range")