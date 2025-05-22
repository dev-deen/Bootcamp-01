my_tuple = (1, 2, 3, 2, 4, 5, 4, 6, 3)
repeated = set()
for item in my_tuple:
    if my_tuple.count(item) > 1:
        repeated.add(item)
print(repeated)
