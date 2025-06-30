#Q4)Convert a dictionary to a list of tuples.
my_dict = {'a': 1, 'b': 2, 'c': 3}
result = []
for key in my_dict:
    result.append((key, my_dict[key]))
print(result)
