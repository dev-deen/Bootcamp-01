class Person:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Name:",self.name)

class Student(Person):
    def __init__(self,name,id):
        super().__init__(name)
        self.id=id
    def display(self):
        super().display()
        print("Student id:",self.id)
s=Student("Anam","001")
s.display()