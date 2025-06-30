data = {
    'apple': 10,
    'banana': 5,
    'orange': 3,
    'mango': 8
}
n = 6
filtered = {key: value for key, value in data.items() if value >= n}
print(filtered)

