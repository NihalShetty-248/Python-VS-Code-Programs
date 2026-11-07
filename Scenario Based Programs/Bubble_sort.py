"""This programs performs Bubble Sort"""


def bubble_sort(collection):

    length = len(collection)

    for i in range(length, 0, -1):
        swapped = False
        for j in range(1, length):
            if collection[j] < collection[j - 1]:
                collection[j - 1], collection[j] = collection[j], collection[j - 1]
                swapped = True

        if not swapped:
            return f"Collection sorted!!\nSorted collection: {collection}"

    else:
        return f"Collection sorted!!\nSorted collection: {collection}"


collection = eval(input("Enter unordered collection: "))
print(bubble_sort(collection))
