def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True
    
print(is_pangram("abc de fghijk lmno pq rstu vw x yz"))
