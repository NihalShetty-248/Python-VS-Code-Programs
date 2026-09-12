n = int(input("Enter a number(>0): "))
i = 1
sum = 0
while i <= n:
    sum += 1 / i
    i += 1
print(f"The sum of series is {sum}")
