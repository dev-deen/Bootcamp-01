#Sort a dictionary by key

d = {4: 'a',1: 'b',5: 'c',2: 'd',3: 'e'}
sort = sorted(d)
s = {}
for key_element in sort:
    s[key_element] = d[key_element]
print(s)

