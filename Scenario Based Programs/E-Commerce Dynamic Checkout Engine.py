"""E-Commerce Dynamic Checkout Engine
Task: Write process_checkout(*prices, tax_rate=0.18, **discounts)"""


def process_checkout(*prices, tax_rate=0.18, **discounts):
    subtotal = sum(prices)
    discount_price = sum(discounts.values())
    final_price = max(0, (subtotal - discount_price) * (1 + tax_rate))
    return round(final_price, 2)


entry = True
while entry:
    item_n = int(input("enter number of items: "))
    price_lst = []
    for i in range(item_n):
        price = float(input(f"Enter price of item {i+1}: "))
        price_lst.append(price)

    tax_rate = float(input("Enter tax rate [press 0 to consider default value]:"))

    disc_dict = {}
    disc_n = int(input("Enter number of discounts: "))
    for i in range(disc_n):
        key, value = eval(input("Enter name and discount [name,disc]: "))
        disc_dict[key] = value

    if tax_rate == 0:
        print(f"\t Total price: {process_checkout(*price_lst,**disc_dict)}\n")
    else:
        print(
            f"\t Total price: {process_checkout(*price_lst,tax_rate=tax_rate,**disc_dict)}\n"
        )

    ch = input("Do you want to continue (y/n): ").lower()
    if ch == "y":
        entry = True
    else:
        entry = False
