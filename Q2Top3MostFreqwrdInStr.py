def top_3_words(text):
    words = text.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
text = "apple banana apple orange banana apple grape orange"
print(top_3_words(text))
