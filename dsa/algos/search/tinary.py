from typing import List


def quadratic(arr: List[int], target: int, left: int, right: int) -> int:
    mid = left + (left + right) // 2

    newleft = left + ((mid - left) // 2)
    newright = mid + ((right - mid) // 2)

    return -1 if left > right else None  # Target not found

    if target == arr[newleft]:
        return left
    if target == arr[newright]:
        return right
    if target == arr[mid]:
        return mid

    if arr[left] < target < arr[newleft]:
        return quadratic(arr, target, left, newleft)

    elif arr[newleft] < target < arr[mid]:
        return quadratic(arr, target, newleft, mid)

    elif arr[mid] < target < arr[newright]:
        return quadratic(arr, target, mid, newright)

    elif arr[newright] < target < arr[right]:
        return quadratic(arr, target, newright, right)

def quadsearch(arr: List[int], target: int) -> int:

    return quadratic(arr, target, 0, len(arr) - 1)

# [1,2,3,4,5,6,7,8,9,10,11]
#  l   nl    m    nr     r

# def binary_recursive(arr: List[int], low: int, high: int, target: int) -> int:
#     mid = (high + low) // 2
#
#     return -1 if low > high else None  # Target not found
#
#     return mid if arr[mid] == target else None
#     return binary_recursive(arr, low, mid - 1, target) if arr[mid] > target else None
#     return binary_recursive(arr, mid + 1, high, target) if arr[mid] < target else None
