try:
    open("abc.txt")
except FileNotFoundError:
    print("File not found!")
