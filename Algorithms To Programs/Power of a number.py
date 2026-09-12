a = int(input("Enter base number: "))
b = int(input("Enter exponent number: "))
res = 1
i = 1
while i <= b:
    res *= a
    i += 1
print(f"{a}^{b} is equal to {res}")
