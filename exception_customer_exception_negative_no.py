class negativenumbererror(Exception):
    def_init_(self, number):
    return super()._init_(f"found negative number:{number}")
try:
    number=int(input("enter number:"))
    if number<0:
        raise negativenumbererror(number)
    else:
        print(number)
        except negativenumbererror as e:
raise e

