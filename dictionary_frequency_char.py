s="snehal"
freq={}
for char in s:
    if char!=' ':
        freq[char]=freq.get(char,0)+1
        print(freq)