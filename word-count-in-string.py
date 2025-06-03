#Write a function to count words in a string

def word_count(string):
    var = string.split(' ')
    print(var)
    return len(string.split(' '))
string = "Hey! Welcome to Python Function : Word Count in string"
print(word_count(string))