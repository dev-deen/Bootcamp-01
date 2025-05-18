#Capitalize the first letter of each word in a string
s = input("Enter string: ")
if s[0].islower():
    print(s[0].upper()+s[1:])
else:
    print(s)
    
'''

Enter string: taiba
Taiba

Enter string: Taiba
Taiba

'''