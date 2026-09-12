num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
i = 1
while i <= min(num1, num2):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
    i += 1
print(f"The GCD of {num1} and {num2} is {gcd}")
