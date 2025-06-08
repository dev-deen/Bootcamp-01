class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id
p = Person("mahek", 19)
print(p.name, p.age,)
s = Student("taiba", 20, "S101")
print(s.name, s.age, s.id)
