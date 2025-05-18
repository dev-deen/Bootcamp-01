#Replace all occurrences of a substring in a string
s = input("Enter a string: ") 
r = input("Enter string to replace : ")
n = input("Enter new substring: ")
o = s.replace(r, n)
print(f"entered string \n {s}")
print(f"Replaced string \n {o}")


'''

Enter a string: my password is T123
Enter string to replace : T123
Enter new substring: ****
entered string 
 my password is T123
Replaced string 
 my password is ****

 '''