num = [12, 35, 1, 10, 34, 1]
unique_num = list(set(num))
if len(unique_num) < 2:
    print("There is no second largest number.")
else:
    unique_num.sort()
    print("Second largest number is:", unique_num[-2])
