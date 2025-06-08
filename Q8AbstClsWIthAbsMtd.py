class Animal:
    def sound(self):
        raise NotImplementedError("Subclass must implement this method")
class Dog(Animal):
    def sound(self):
        print("Bark")
d = Dog()
d.sound()
