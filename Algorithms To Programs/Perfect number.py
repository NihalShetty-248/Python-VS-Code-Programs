n = int(input("Enter a number: "))
i = 1
sum = 0
while i < n:
    if n % i == 0:
        sum += i
    i += 1
if sum == n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")
