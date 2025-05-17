m = input("Enter a string: ")
count = 0
for c in m:
    if c in 'aeiouAEIOU':
        count += 1
print(count)
