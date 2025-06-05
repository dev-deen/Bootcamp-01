#Create a custom exception for negative numbers

class NegativeNumberError(Exception):
    
    def __init__(self, number):
        return super().__init__(f"Found Negative Number: {number}")

try:
    
    number = int(input("Enter Number: "))
    if number < 0:
        raise NegativeNumberError(number)
    else:
        print(number)
except NegativeNumberError as e:
    raise e
