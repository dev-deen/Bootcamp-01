#Count occurrences of an element in a list

l = [1,2,3,4,4,5,4,6,6,7,6,7,6,7,8,5,9,0]
a = int(input("Enter number to find: "))
count = 0
for i in l:
    if i == a:
        count += 1
print(f"Count of {a} in list {l} is {count}")

'''
Enter number to find: 7
Count of 7 in list [1, 2, 3, 4, 4, 5, 4, 6, 6, 7, 6, 7, 6, 7, 8, 5, 9, 0] is 3
'''
