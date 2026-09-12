cp = float(input("Enter cost price: "))
sp = float(input("Enter sale price: "))
if sp > cp:
    print(f"Profit of Rs.{sp-cp}")
else:
    print(f"Loss of Rs.{cp-sp}")
