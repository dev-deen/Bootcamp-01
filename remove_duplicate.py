list=[1,2,3,3,4]
unique_list=[]
for item in list:
    if item not in unique_list:
        unique_list.append(item)
        print(unique_list)