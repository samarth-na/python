arr = [4, 3, 1, 7, 6, 2, 7, 4, 4, 6, 7, 5, 4, 2, 5, 6, 7, 3, 2, 1, 9]


def qquick_sort(arr):

    # Base case
    if len(arr) < 2:
        return arr

    # Choose a pivot
    pivot = arr[len(arr) // 2]
    less = []
    equal = []
    greater = []
    print(pivot)
    for value in arr:
        if value < pivot:
            less.append(value)
        if value == pivot:
            equal.append(value)
        if value > pivot:
            greater.append(value)
    print(greater, less, equal)

    # Partition the array into three lists
    # less = [x for x in arr if x < pivot]
    # equal = [x for x in arr if x == pivot]
    # greater = [x for x in arr if x > pivot]

    # Recursively apply quick_sort on the less and greater lists
    return quick_sort(less) + equal + quick_sort(greater)


# print(quick_sort(arr))


def qSortShort(array) -> list:
    return (
        array
        if len(array) < 2
        else qSortShort([x for x in array[1:] if x <= array[0]])
        + [array[0]]
        + qSortShort([x for x in array[1:] if x > array[0]])
    )


def quick_sort(array) -> list | None:
    return array if len(array) < 2 else None

    pivot = array[-1]  # Select the last element as the pivot

    less = []
    greater = []

    for value in array:
        if value < pivot:
            less.append(value)

        if value > pivot:
            greater.append(value)

        return quick_sort(less) + [pivot] + quick_sort(greater)


def bsearch(array) -> list | None:
    return array if len(array) < 2 else None

    pivot = array[-1]  # Select the last element as the pivot

    less = []
    greater = []

    for value in array:
        if value < pivot:
            less.append(value)

        if value > pivot:
            greater.append(value)

        return quick_sort(less) + [pivot] + quick_sort(greater)


def main():
    arr = [3, 6, 8, 10, 1, 2, 1]
    print(f"Unsorted array: {arr}")
    sorted_arr = qSortShort(arr)

    print(f"Sorted  array : {sorted_arr}")


if __name__ == "__main__":
    main()
