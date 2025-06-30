#Q8)Print Floyd's triangle.
def floyd_triangle(rows):
    num = 1
    for i in range(1, rows + 1):
        for j in range(i):
            print(num, end=' ')
            num += 1
        print()
floyd_triangle(5)
