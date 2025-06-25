def chunk_list(lst, n):
    chunks = []
    for i in range(0, len(lst), n):
        chunk = []
        for j in range(i, min(i + n, len(lst))):
            chunk.append(lst[j])
        chunks.append(chunk)
    return chunks
print(chunk_list([1, 2, 3, 4, 5, 6, 7], 3))

#Sir's Approach:
arr = [1, 2, 3, 4,  5, 6, 7, 8, 9]
chunk = 3
def divide_list(arr, chunk):
    ans = []
    for i in range(0, len(arr), chunk):
        new_list = arr[i: i+chunk]
        ans.append(new_list)
    return ans
print(divide_list(arr, chunk))