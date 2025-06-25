def find_pairs(nums, target):
    result = []
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                result.append((nums[i], nums[j]))
    return result
nums = [1, 2, 3, 4, 5]
target = 6
print(find_pairs(nums, target))
