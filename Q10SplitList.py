arr = [1, 6, 11, 5]
arr.sort()
part1 = arr[:len(arr)//2]
part2 = arr[len(arr)//2:]
print("Part 1:", part1, "Sum:", sum(part1))
print("Part 2:", part2, "Sum:", sum(part2))
print("Difference:", abs(sum(part1) - sum(part2)))
