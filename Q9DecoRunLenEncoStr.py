#Q9)Decode a run-length encoded string.
def run_length_decode(s):
    result = ""
    count = ""
    for char in s:
        if char.isalpha():
            if count:  
                result += prev_char * int(count)
                count = ""
            prev_char = char
        else:
            count += char
    result += prev_char * int(count)
    return result
print(run_length_decode("a3b2c3"))
