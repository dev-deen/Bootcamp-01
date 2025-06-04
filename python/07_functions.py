def word_count(string):
    var=string.split(' ')
    print(var)
    return len(string.split(' '))
string='hello everyone welcome'
print(word_count(string))