class Animal:
    def sound(self):
        raise NotImplementedError("Subclass implement this method")
class cat(Animal):
    def sound(self):
        print("meow")
d = cat()
d.sound()