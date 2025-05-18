#Count the number of vowels in a string
s = input("Enter a string: ") 
count = 0
for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        count += 1

print(f"number of vowels in string {s} is {count}")

'''

Enter a string: taiba
number of vowels in string taiba is 3

'''