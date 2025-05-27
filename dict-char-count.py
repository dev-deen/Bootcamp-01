#Count frequency of each character in a string using dictionary

string_x = input("enter string: ")
count_x = {}

for char in string_x:
    if char in count_x:
        count_x[char] += 1
    else:
        count_x[char] = 1

print(count_x)