#Sum all values in a dictionary

dictionary = {
    'Taiba':50000,
    'Mahek':80000,
    'Duaa':80500
}
sum_values = sum(dictionary.values())
print(sum_values)

'''
or
'''
result = 0
for v in dictionary.values():
    result = result + v
print(result)