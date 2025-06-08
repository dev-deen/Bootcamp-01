class MyClass:
    count = 0
    @classmethod
    def show(cls):
        print("This is a class method")
    @staticmethod
    def hello():
        print("This is a static method")
MyClass.show()
MyClass.hello()
