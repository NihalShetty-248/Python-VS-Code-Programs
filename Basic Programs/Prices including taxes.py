amt = float(input("Enter price without tax: "))
tax = float(input("Enter tax as percentage:"))
print(f"The final price including taxes is {amt+(amt*tax/100)}")
