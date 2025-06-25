nested_list = [1, 2, 3, [1, 2], [1, 2, [1, 3, 4]]]
def flatten_list(nested_list):
    new_list =[]
    for element in nested_list:
        if isinstance(element, list):
            new_list.extend(flatten_list(element))
        else:
            new_list.append(element)
    return new_list
print(flatten_list(nested_list))