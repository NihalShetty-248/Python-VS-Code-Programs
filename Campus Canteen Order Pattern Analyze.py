"""Campus Canteen Order Pattern Analyzer
This program takes the lsit of orders as input and prints
 The total number of burgers ordered.
 The total number of sandwiches ordered.
 The total number of French fries ordered.
 The total number of pizzas ordered.
 The total number of cold coffees ordered.
 The total number of juices ordered.
 Which item was the most frequently ordered.
 The percentage of all orders that were either Burger or Pizza.
 whether the observation represents a 'heavy fast-food period' or a 'normal period'"""

num = int(input("Enter number of items: "))
item_dict = {
    "B": "Burger",
    "S": "Sandwich",
    "F": "French Fries",
    "P": "Pizza",
    "C": "Cold Coffee",
    "J": "Juice",
}

# To input items
item_list = []
for i in range(1, num + 1):
    item = input(f"Enter item {i}: ").upper()
    item_list.append(item)

burger = item_list.count("B")
sandwich = item_list.count("S")
french_fries = item_list.count("F")
pizza = item_list.count("P")
cold_coffee = item_list.count("C")
juice = item_list.count("J")

# Frequently Ordered item
max = 0
frequent_item = ""
for i in item_list:
    if item_list.count(i) >= max and i not in frequent_item:
        if item_list.count(i) == max:
            frequent_item = frequent_item + ", " + item_dict[i]
        else:
            frequent_item = item_dict[i]
            max = item_list.count(i)

percentage = ((burger + pizza) / num) * 100

print(f"Number of burgers: {burger}")
print(f"Number of sandwiches: {sandwich}")
print(f"Number of french fries: {french_fries}")
print(f"Number of pizzas: {pizza}")
print(f"Number of cold coffee: {cold_coffee}")
print(f"Number of juices: {juice}")
print(f"Most frequent items is/are: {frequent_item}")
print(f"Percentage of burger + pizza: {percentage}")

# Observation classification
if percentage >= 40 and burger + pizza >= 5:
    print("Heavy Fast food period")
else:
    print("Normal period")
