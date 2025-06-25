#Q6)Encode a string using Caesar cipher.
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char  
    return result
text = "hello world"
shift = 3
print(caesar_cipher(text, shift))
