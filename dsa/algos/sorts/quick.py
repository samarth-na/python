arr = [4, 3, 1, 7, 6, 2, 7, 4, 4, 6, 7, 5, 4, 2, 5, 6, 7, 3, 2, 1, 9]


def quick_sort(arr):
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


def quick_sort2(array):
    if len(array) < 2:
        return array

    print(array)
    pivot = array[-1]  # Select the last element as the pivot
    print(f"Pivot: {pivot}")
    less = []
    greater = []

    for value in array:
        if value < pivot:
            less.append(value)
        if value > pivot:
            greater.append(value)

    # Debugging print statements

    return quick_sort2(less) + [pivot] + quick_sort2(greater)


# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort2(arr)

print(f"Sorted array: {sorted_arr}")
