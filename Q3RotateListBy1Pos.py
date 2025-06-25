def rotate_right(list):
    return [list[-1]] + list[:-1]
print(rotate_right([1, 2, 3, 4]))

#rotate left by 1:
def rotate_left(list):
    return list[1:] + [list[0]]
print(rotate_left([1, 2, 3, 4]))

#using for loop:
x = [1, 2, 3, 4]
def rotate(arr):
    prev = arr[-1]
    for i in range(len(arr)):
        prev, arr[i] = arr[i], prev
    print(arr)
rotate(x)


    