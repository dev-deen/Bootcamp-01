#Check if a string is a palindrome
x = input("Enter String: ")
rev = x[::-1]
if rev == x:
    print(f"String {x} is palindrome")
else:
    print(f"String {x} is not a palindrome")
    
'''

Enter String: taiba
String taiba is not a palindrome

Enter String: mom 
String mom  is not a palindrome

'''