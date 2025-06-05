#Write a program that retries on exception

class AgeValidationError(Exception):
    
    def __init__(self, age):
        return super().__init__(f"{age} comes in under age category, Sorry u are not Valid")

while True:
    
    age = int(input("Enter ur age: "))
    print(age)
    try:
        
        if age < 18:
            raise AgeValidationError(age)
            continue
        else:
            print(f"{age} is Valid")
            break
    except AgeValidationError as e:
        print(e)
 