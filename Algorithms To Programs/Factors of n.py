n = int(input("Enter a number: "))
i = 1
print(f"The factors of {n} are:")
while i <= n:
    if n % i == 0:
        print(i)
    i += 1
