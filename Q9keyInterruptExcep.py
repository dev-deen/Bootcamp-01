try:
    while True:
        name = input("Enter your name: ")
        print("Hello,", name)
except KeyboardInterrupt:
    print("\nProgram stopped by user.")
