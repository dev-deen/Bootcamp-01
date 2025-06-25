x = [1, 2, 3, 5]
def find_missing(arr):
    sum_x = sum(arr)
    n = len(arr) + 1
    math_sum = n * (n + 1) // 2  #math formula
    return math_sum - sum_x
ans = find_missing(x)
print(ans)