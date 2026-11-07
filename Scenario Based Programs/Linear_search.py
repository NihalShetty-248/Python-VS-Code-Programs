"""The following program performs Linear Search"""


def linear_search(required_item, collection):
    length = len(collection)
    for index in range(length):
        if collection[index] == required_item:
            return f"Found {required_item} at index {index}"

    else:
        return f"{required_item} does not exist in the collection"


collection = eval(input("Enter collection: "))
required_item = eval(input("Enter item to be found: "))
print(linear_search(required_item, collection))
