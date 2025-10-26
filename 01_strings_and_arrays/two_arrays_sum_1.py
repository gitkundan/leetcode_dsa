"""
# Two-Pointer Technique Guide

## When to Use:
- Comparing or processing two sequences simultaneously
- Typically used with sorted arrays or linked lists
- Common in problems involving pairs or sequence alignment

## How It Works:
1. **Initialization**:
   - Create two pointers (indices), one for each sequence
   - Typically start both at beginning (index 0)

2. **Processing Loop**:
   - While both pointers are within their sequence bounds:
     a. Compare elements at current pointer positions
     b. Perform required operation (merge, compare, etc)
     c. Move pointer(s) forward based on comparison result

3. **Completion**:
   - Handle remaining elements in either sequence if needed

## Complexity Analysis:
- **Time**: O(n + m) - Linear in combined size of inputs
- **Space**: O(1) - Constant space for pointers (unless creating new output)

## Key Advantages:
- Single pass through both sequences
- No unnecessary comparisons
- Efficient memory usage
"""

def combine_arrays_without_sorting(arr1: list[int], arr2: list[int]) -> list[int]:
    """
    Concatenates two arrays without sorting.
    Time Complexity: O(1) - Simple array concatenation
    Space Complexity: O(n+m) - Creates new array with all elements
    """
    return arr1 + arr2


def combine_arrays_with_sorting(arr1: list[int], arr2: list[int]) -> list[int]:
    """
    Merges two sorted arrays into one sorted array using two-pointer technique.
    
    Args:
        arr1: First sorted array of integers
        arr2: Second sorted array of integers
    
    Returns:
        Merged sorted array containing all elements from both inputs
    
    Time Complexity: O(n+m) - Each element is processed exactly once
    Space Complexity: O(n+m) - Creates new array with all elements
    """
    result: list[int] = []
    i = j = 0  # Initialize pointers for both arrays
    
    # Merge while both arrays have elements remaining
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # Add any remaining elements from arr1
    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    # Add any remaining elements from arr2
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
        
    return result


# Example usage with sorted inputs to demonstrate merging
if __name__ == "__main__":
    arr1 = sorted([1, 4, 2, 0, 1])  # [0, 1, 1, 2, 4]
    arr2 = sorted([5, 6, 7])        # [5, 6, 7]
    result = combine_arrays_with_sorting(arr1, arr2)
    print(f"Merged sorted array: {result}")
