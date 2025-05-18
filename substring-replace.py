#Replace all occurrences of a substring in a string
s = input("Enter a string: ") 
r = input("Enter string to replace : ")
n = input("Enter new substring: ")
o = s.replace(r, n)
print(f"entered string \n {s}")
print(f"Replaced string \n {o}")


'''

Enter a string: Ananas
Enter string to replace : an
Enter new substring: t
entered string 
 Ananas
Replaced string 
 Antas

 '''
