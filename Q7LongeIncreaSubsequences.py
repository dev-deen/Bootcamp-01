def longest_increasing_subsequence(nums):
    if not nums:
        return []
    longest = []
    for i in range(len(nums)):
        current = [nums[i]]
        for j in range(i + 1, len(nums)):
            if nums[j] > current[-1]:
                current.append(nums[j])
        if len(current) > len(longest):
            longest = current
    return longest
nums = [10, 1, 2, 5, 3, 7, 8]
print(longest_increasing_subsequence(nums))

