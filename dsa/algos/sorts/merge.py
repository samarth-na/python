def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Find the middle point and divide the array
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    # Merge the two arrays into result
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Collect the remaining elements
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


# Example usage:
arr = [8, 3, 5, 4, 7, 6, 1, 2]
sorted_arr = merge_sort(arr)
print(sorted_arr)
