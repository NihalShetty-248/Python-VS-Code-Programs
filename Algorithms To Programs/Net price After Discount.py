price = float(input("Enter price: "))
disc = float(input("Enter discount: "))
net_price = price - (price * (disc / 100))
print(f"The net price is {net_price}")
