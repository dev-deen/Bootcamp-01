#Q5)Find the most frequent character in a string.
s = "apple"
most = max(set(s), key = s.count)
print("Most frequent character:", most)
