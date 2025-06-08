# Step 1: Create custom exception
class NegativeNumberError(Exception):
    pass
try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise NegativeNumberError
    print("Positive number:", num)
except NegativeNumberError:
    print("Error: Negative number not allowed!")
