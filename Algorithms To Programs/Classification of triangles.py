x = float(input("Enter side 1: "))
y = float(input("Enter side 2: "))
z = float(input("Enter side 3: "))
if x == y and y == z:
    print("Equilateral")
elif x == y or y == z or z == x:
    print("Isosceles")
else:
    print("scalene")
