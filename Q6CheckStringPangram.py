def is_pangram(sentence):
    sentence = sentence.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in sentence:
            return False
    return True
print(is_pangram("The quick brown fox jumps over a lazy dog.")) 
