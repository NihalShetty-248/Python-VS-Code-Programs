"""Food Ordering System
The following program asks the user for their order continuously until they enter done.
It calculates:
    The total Bill
    A 10% discount if the price is more than Rs.500
    Prints the bill"""

name = input("Enter name: ")
print(
    "MENU",
    "Burger - Rs.120",
    "Pizza - Rs.250",
    "Sandwich - Rs.100",
    "Juice - Rs.60",
    sep="\n",
)
entry = True
price = 0
while entry:
    item = input('Enter item ("Done" for exit): ').lower()

    if item == "burger":
        price += 120
    elif item == "pizza":
        price += 250
    elif item == "sandwich":
        price += 100
    elif item == "juice":
        price += 60
    elif item == "done":
        entry = False
    else:
        print("INVALID ITEM !! Try again")

print(f"Customer: {name}")
print(f"Total: Rs.{price}")

if price >= 500:
    discount = price * 0.1
else:
    discount = 0

print(f"Discount: Rs.{discount}")
print(f"Final Bill: Rs.{price-discount}")
