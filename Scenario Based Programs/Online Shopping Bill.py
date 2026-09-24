"""Online Shopping Bill
This program asks the user price for a certain number of times
and returns the amount of discount applicable:
    Below ₹1,000: No discount
    ₹1,000-₹4,999: 10% discount
    ₹5,000 and above: 20% discount"""

n = int(input("Enter number of products: "))
price_sum = 0
for i in range(n):
    price = float(input("Enter price: "))
    price_sum += price

if price_sum < 1000:
    discount = 0
elif 1000 <= price_sum <= 4999:
    discount = 10
else:
    discount = 20

final_bill = price_sum * (1 - discount / 100)

print(f"Total: Rs. {price_sum}")
print(f"Discount: Rs. {(discount*price_sum)/100}")
print(f"Final bill: Rs. {final_bill}")
