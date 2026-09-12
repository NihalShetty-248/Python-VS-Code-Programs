num = int(input("Enter a number: "))
sum = 0
n = num
pow = len(str(num))
while n > 0:
    digit = n % 10
    sum += digit**pow
    n = n // 10
if sum == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
