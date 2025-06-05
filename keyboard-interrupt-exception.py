#Handle keyboard interrupt exception

try:
    print ("Keep Typing... press Ctrl C to terminate.")
    x = input("Write a sentence : ")
    print(x)
except KeyboardInterruptError:
    print("U decided to terminate ur program")
finally:
    print("Program Terminated")