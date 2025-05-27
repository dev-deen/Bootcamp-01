my_dict={'b':2,'a':1}
sorted_value=dict(sorted(my_dict.items(),key=lambda item:item[1]))
print(sorted_value)