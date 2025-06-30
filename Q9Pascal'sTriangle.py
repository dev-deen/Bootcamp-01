#Q9)Print Pascal's triangle.

def pascal_triangle(n):
    for i in range(n):
        num = 1
        print(' ' * (n - i), end='')  # for alignment
        for j in range(i + 1):
            print(num, end=' ')
            num = num * (i - j) // (j + 1)
        print()
pascal_triangle(5)
