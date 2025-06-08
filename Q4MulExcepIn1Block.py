try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except (ZeroDivisionError, ValueError):
    print("Error: You entered zero or an invalid number!")
