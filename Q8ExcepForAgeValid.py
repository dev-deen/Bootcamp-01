class InvalidAge(Exception):
    pass
try:
    age = int(input("Enter age: "))
    if age < 0:
        raise InvalidAge
    print("Age is valid:", age)
except InvalidAge:
    print("Error: Age can't be negative!")
except ValueError:
    print("Error: Please enter a number!")
