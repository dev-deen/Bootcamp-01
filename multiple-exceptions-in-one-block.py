#Handle multiple exceptions in one block

#Handle multiple exceptions in one block

try:
    l = [1,2,3,4,5]
    a = int(input("Enter Index value from list to Divide: "))
    b = int(input("Enter Number to Divide: "))
    div = l[a]/b
    print(div)
except IndexError:
    print("Index Value Does Not Exist")
except ZeroDivisionError:
    print("Division By Zero is Not Acceptable")
 