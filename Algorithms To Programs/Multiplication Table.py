num = int(input("Enter a number: "))
n = int(input("Enter until which number you need the multiplication table: "))
print(f"The multiplication table of {n} is: ")
i = 1
while i <= n:
    print(f"{i}x{num}={i*num}")
    i += 1
