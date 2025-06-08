def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Can't divide by zero!")
    else:
        print("Result is:", result)
    finally:
        print("Done!")
divide(8, 2)

