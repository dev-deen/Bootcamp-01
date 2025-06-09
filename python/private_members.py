class student:
    def __init__(self):
        self.__name=""
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    
s=student()
s.set_name("Anam")
print("Name :",s.get_name())