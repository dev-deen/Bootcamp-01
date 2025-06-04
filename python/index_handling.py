try:
    list=[1,2,3]
    print(list[5])
except IndexError as e:
    print("Index not found")