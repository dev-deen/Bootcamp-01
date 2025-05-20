#Remove duplicates from a list

l = [1,2,3,4,4,5,3,5,6,7,66,7,6,5,23,1,2]
result = set(l)
print(f"List with Duplicate values: {l}")
print(f"List without Duplicate values: {result}")


'''

List with Duplicate values: [1, 2, 3, 4, 4, 5, 3, 5, 6, 7, 66, 7, 6, 5, 23, 1, 2]
List without Duplicate values: {1, 2, 3, 4, 5, 6, 7, 66, 23}

'''