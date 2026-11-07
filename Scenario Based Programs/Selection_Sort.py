"The following program performs Selection Sort"


def selection_sort(collection):
    length = len(collection)

    for i in range(length):
        min_index = i
        for j in range(i, length):
            if collection[j] < collection[min_index]:
                min_index = j

        collection[i], collection[min_index] = collection[min_index], collection[i]

    return f"Collection Sorted!!\nSorted collection: {collection}"


collection = eval(input("Enter an unordered collection: "))
print(selection_sort(collection))
