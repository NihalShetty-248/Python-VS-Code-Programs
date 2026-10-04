"""This program takes a 'list' and a 'size' as an argument and
splits the 'list' into smaller sub-list that that contain utmost 'size' elements"""

inventory_items = eval(input("Enter list of items: "))
chunk_size = int(input("Enter max size of each chunk: "))
chunk_items = []

for i in range(0, len(inventory_items), chunk_size):
    chunk_items.append(inventory_items[i : i + chunk_size])
print(chunk_items)
print()

# Alternate method
chunk_items = [
    inventory_items[i : i + chunk_size]
    for i in range(0, len(inventory_items), chunk_size)
]
print(chunk_items)
