#Q7)Decode a Caesar cipher encoded string.
def caesar_decipher(text, shift):
    result = ""
    for char in text:
        if char.islower():
            result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            result += char  
    return result
encoded = "khoor zruog"
shift = 3
print(caesar_decipher(encoded, shift))
