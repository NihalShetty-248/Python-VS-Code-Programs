x1, y1 = eval(input("Enter initial coordinates: "))
x2, y2 = eval(input("Enter final coordinates: "))
dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
print(f"The distance is {dist}")
