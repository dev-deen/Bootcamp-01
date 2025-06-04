class AgeValidationError(Exception):
    def __init__(self,age):
        super().__init__(f"age:{age} is not valid")

try:
    age=int(input("enter your age:"))
    if age<18:
        raise AgeValidationError(age)
    else:
        print("age is valid")

except AgeValidationError as e:
    raise e