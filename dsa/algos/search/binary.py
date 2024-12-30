from typing import List


#
#
def binary_iterative(arr: List[int], target: int) -> int:
    low = 0
    high = len(arr) - 1

    while arr[low] <= arr[high]:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found


def binary_recursivee(arr: List[int], low: int, high: int, target: int) -> int:
    return (
        -1
        if low > high
        else (mid := (low + high) // 2)
        if arr[mid := (low + high) // 2] == target
        else binary_recursive(arr, low, mid - 1, target)
        if arr[mid] > target
        else binary_recursive(arr, mid + 1, high, target)
    )


def binary_recursive(arr: List[int], low: int, high: int, target: int) -> int:
    mid = (high + low) // 2

    return -1 if low > high else None  # Target not found

    return mid if arr[mid] == target else None
    return binary_recursive(arr, low, mid - 1, target) if arr[mid] > target else None
    return binary_recursive(arr, mid + 1, high, target) if arr[mid] < target else None


# Example usage
# arr = [1, 3, 5, 7, 9]
# target = 5
# result = binary_recursive(arr, 0, len(arr) - 1, target)
# print("Index:", result)

for i in range(1, 10, 1):
    print(i)
    pass
