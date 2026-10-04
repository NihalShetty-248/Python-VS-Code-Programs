"""The following problem is used to update the cart of a user and find the total price
The cart and price of each item is already defined in the form of a list
The task is: A customer adds "bread" to their 'cart'
             removes "banana" from 'cart'
             adds the bread price (2.00) to the 'prices' list
             removes the banana price (0.75) from the 'price' list
             Compute and print the total cost."""

cart = ["apple", "banana", "milk"]
prices = [1.50, 0.75, 2.50]

print('Adding "bread" to cart...')
cart.append("bread")

print('Removing "banana" from cart...')
cart.remove("banana")

print("Adding price of bread (2.00) to prices...")
prices.append(2.00)

print("Removin price of banana (0.75) from prices...")
prices.remove(0.75)

print(cart)
print(f"Total cost is Rs. {sum(prices)}")
