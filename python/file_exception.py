try:
    file=open('file.txt','r')
    data=file.read()
    print(data)
except FileNotFoundError as e:
    print("file not found...!")