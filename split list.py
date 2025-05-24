list_x = [1,2,3,4,5]
list_x.sort()
total_sum = sum(list_x)
left_sum = 0
dictionary = {}
for i in range(0,len(list_x)):
    left_sum += list_x[i]
    right_sum = total_sum - left_sum
    curr_diff = abs(right_sum - left_sum)
    dictionary[curr_diff] = i
print(dictionary)
print(min(dictionary))