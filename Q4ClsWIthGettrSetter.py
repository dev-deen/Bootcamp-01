class Person:
    def __init__(self, name, age):
        self.__name = name   
        self.__age = age     
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive!")
p = Person("mahek", 19)
print(p.get_name())  
p.set_age(30)
print(p.get_age())   
p.set_age(-5)        