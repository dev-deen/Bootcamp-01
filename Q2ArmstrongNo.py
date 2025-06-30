#Q2)Check if a number is Armstrong number.
num = int(input("Enter a number: "))
n = len(str(num))
sum = 0
for digit in str(num):
    sum += int(digit) ** n
if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
