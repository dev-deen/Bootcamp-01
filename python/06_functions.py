def is_pangram(string):
    string=string.lower()
    alpha_count=0
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char in string:
            alpha_count+=1
    return alpha_count==26
    
print(is_pangram("thequickbrownfoxjumpsoverthelazydog"))