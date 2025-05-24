numbers = [5, 3, 8, 1, 9, 2, 7, 4]


mid = len(numbers) // 2
first_half = numbers[:mid]
second_half = numbers[mid:]


first_half_sorted = sorted(first_half)
second_half_sorted = sorted(second_half)

print("First half sorted:", first_half_sorted)
print("Second half sorted:", second_half_sorted)
