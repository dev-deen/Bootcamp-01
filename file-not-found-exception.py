#Handle file not found exception
try:
    file1 = open("PythonFile.txt","r")
    content1 = file1.read()
    print(content1)
    file1.close()
    file2 = open("PythonFile001.txt","r")
    content2 = file2.read()
    print(content1)
    file2.close()
except FileNotFoundError:
    print("File does not exist")
except NameError:
    print("Incorrect or no file defined")