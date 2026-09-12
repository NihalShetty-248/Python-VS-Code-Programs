n = int(input("Enter a number: "))
isPrime = True
i = 2
while i <= n / 2:
    if n % i == 0:
        isPrime = False
        break
    i += 1
if isPrime:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")
