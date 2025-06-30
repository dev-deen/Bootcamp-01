#Q3)Merge list of dictionaries with common keys.
def merge_dictionary(dict_list):
    ans = {}
    for d in dict_list:
        for key in d:
            if key in ans:
                ans[key] += d[key]
            else:
                ans[key] = d[key]
    return ans
dicts = [{'a': 1, 'b': 2}, {'a': 3, 'b': 1}, {'a': 2, 'c': 4}]
print(merge_dictionary(dicts))
