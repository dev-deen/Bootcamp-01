#Create a custom exception for age validation

class AgeValidationError(Exception):
    
    def __init__(self, age):
        return super().__init__(f"{age} comes in under age category, Sorry u are not Valid")

try:
    
    age = int(input("Enter ur age: "))
    if age < 18:
        raise AgeValidationError(age)
    else:
        print(f"{age} is Valid")
except AgeValidationError as e:
    print(e)
