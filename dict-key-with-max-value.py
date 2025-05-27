#Find the key with the maximum value in a dictionary

my_dict = {'a': 10, 'b': 50, 'c': 30}
max_key = max(my_dict, key=my_dict.get)
print(max_key)