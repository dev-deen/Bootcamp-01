#Q5)Find keys with duplicate values in a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
duplicates = {}
for key in my_dict:
    val = my_dict[key]
    if val in duplicates:
        duplicates[val].append(key)
    else:
        duplicates[val] = [key]
for val in duplicates:
    if len(duplicates[val]) > 1:
        print("Value:", val, "→ Keys:", duplicates[val])
