class NegativeNumberException(Exception): 
    def __init__(self,number):
        return super().__init__(f"found negative number:{number}")
   
    
try:
    number =int(input("enter a number"))
    if number<0:
        raise NegativeNumberException(number)
    else:
        print("no error",number)
except NegativeNumberException as e:
    raise e