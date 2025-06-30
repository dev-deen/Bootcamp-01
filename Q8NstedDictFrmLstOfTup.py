#Q8)Create a nested dictionary from a list of tuples.

data = [('a', 'x', 1), ('a', 'y', 2), ('b', 'x', 3)]
result = {}
for outer, inner, value in data:
    if outer not in result:
        result[outer] = {}
    result[outer][inner] = value
print(result)
