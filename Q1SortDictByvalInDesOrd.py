#Q1)Sort a dictionary by values in descending order.
def sort_dict_by_values_desc(d):
    items = []
    for key in d:
        items.append((key, d[key]))
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j][1] < items[j + 1][1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    sorted_dict = {}
    for key, value in items:
        sorted_dict[key] = value
    return sorted_dict
data = {'apple': 10, 'banana': 5, 'cherry': 20}
print(sort_dict_by_values_desc(data))
