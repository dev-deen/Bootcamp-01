my_list=[1,2,3,4,5,4,5,2,4,6,4,6,1]
new_list= []
for item in my_list:
    if item not in new_list:
        new_list.append(item)
print(new_list)