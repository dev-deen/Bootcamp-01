#Print multiplication table for a given number
x = int(input("Enter a number: "))
for i in range(1, 11): 
    print(f"{x} × {i} = {x * i}")