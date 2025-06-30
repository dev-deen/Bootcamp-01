keys = ['fruit', 'fruit', 'vegetable', 'vegetable']
values = ['apple', 'banana', 'carrot', 'potato']
{
    'fruit': ['apple', 'banana'],
    'vegetable': ['carrot', 'potato']
}
result = {}
for key, value in zip(keys, values):
    if key not in result:
        result[key] = []
    result[key].append(value)
print(result)

