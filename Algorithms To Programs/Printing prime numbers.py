n = int(input("Enter number: "))
isprime = True
print(f"The prime numbers upto {n} are:")
i = 2
while i <= n:
    j = 2
    while j < i:
        if i % j == 0:
            isprime = False
        j += 1
    if isprime:
        print(i)
    isprime = True
    i += 1
