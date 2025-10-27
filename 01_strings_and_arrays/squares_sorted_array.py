"""
Square and Sort Algorithm Implementations

This module provides different approaches to square each element in a sorted array
and return the results in sorted order.

Key Approaches:
1. Two-pointer technique (O(n) time, O(n) space)
2. Naive square-and-sort (O(n log n) time, O(n) space)

The two-pointer method leverages the sorted input property by comparing extremes.
"""
def square_and_sort(arr: list[int]) -> list[int]:
    """
    Optimized two-pointer approach for sorted squares.

    Args:
        arr: Sorted input array (non-decreasing order)

    Returns:
        list[int]: Squared elements in sorted order

    Time Complexity: O(n) - Single pass through the array
    Space Complexity: O(n) - Creates new result array
    """
    result = [0] * len(arr)
    i = 0  # Left pointer
    j = len(arr) - 1  # Right pointer
    k = len(arr) - 1  # Write pointer

    while i <= j:
        # Compare squared values from both ends
        if arr[i]**2 >= arr[j]**2:
            result[k] = arr[i]**2
            i += 1
        else:
            result[k] = arr[j]**2
            j -= 1
        k -= 1
    return result
def square_and_sort_naive(arr: list[int]) -> list[int]:
    """
    Simple square-then-sort approach for comparison.

    Args:
        arr: Input array (sorted or unsorted)

    Returns:
        list[int]: Squared elements in sorted order

    Time Complexity: O(n log n) due to sorting
    Space Complexity: O(n) for squared values
    """
    return sorted(x**2 for x in arr)
def square_and_sort_listcomp(arr: list[int]) -> list[int]:
    """
    List comprehension version of naive approach.

    Args:
        arr: Input array (sorted or unsorted)

    Returns:
        list[int]: Squared elements in sorted order
    """
    squared = [x**2 for x in arr]
    squared.sort()
    return squared

def square_sort_deque(nums:list[int]):
    from collections import deque
    result = deque()
    left, right = 0, len(nums) - 1

    while left <= right:
        if abs(nums[left]) >= abs(nums[right]):
            result.appendleft(nums[left]**2)
            left += 1
        else:
            result.append(nums[right]**2)
            right += 1

    return list(result)

if __name__ == "__main__":
    test_cases = [
        [-4, -1, 0, 3, 10],
        [-7, -3, 2, 3, 11],
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1]
    ]

    for test in test_cases:
        print(f"Original: {test}")
        print(f"Two-pointer: {square_and_sort(test)}")
        print(f"Naive sorted: {square_and_sort_naive(test)}")
        print(f"Listcomp sorted: {square_and_sort_listcomp(test)}")
        print(f"Listcomp sorted: {square_sort_deque(test)}")
        print()