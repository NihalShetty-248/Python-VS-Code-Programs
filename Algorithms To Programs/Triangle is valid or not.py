a = float(input("Enter side1: "))
b = float(input("Enter side2: "))
c = float(input("Enter side3: "))
if a + b > c and b + c > a and c + a > b:
    print("Valid Triangle")
else:
    print("Invalid Triangle")
