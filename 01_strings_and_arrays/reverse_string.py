"""
Reverse a string in-place using two-pointer technique.

The input string is provided as a list of characters to allow in-place modification.
The algorithm must use O(1) extra memory, meaning it can only use a fixed number
of variables regardless of the input size.

Approaches:
1. Two-pointer technique with explicit character preservation
2. Using temporary variable for swap
3. Python tuple assignment for cleaner swap

Time Complexity: O(n) - Each character is visited once
Space Complexity: O(1) - Only uses pointers and temporary variables
"""

def reverse_string(s: list[str]) -> None:
    """
    Original implementation preserving both characters during swap
    
    Args:
        s: List of characters to be reversed in-place
    """
    i = 0
    j = len(s) - 1
    while i < j:
        a = s[i]  # Preserve start character
        b = s[j]  # Preserve end character
        s[i] = b  # Swap start position
        s[j] = a  # Swap end position
        i += 1
        j -= 1

def reverse_string_v1(s: list[str]) -> None:
    """
    Implementation using temporary variable for swap
    
    Args:
        s: List of characters to be reversed in-place
    """
    left = 0
    right = len(s) - 1
    while left < right:
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        left += 1
        right -= 1

def reverse_string_v2(s: list[str]) -> None:
    """
    Pythonic implementation using tuple assignment
    
    Args:
        s: List of characters to be reversed in-place
    """
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

if __name__ == "__main__":
    # Test all implementations
    test_cases = [
        ["h","e","l","l","o"],
        ["H","a","n","n","a","h"]
    ]
    
    for func in [reverse_string, reverse_string_v1, reverse_string_v2]:
        for case in test_cases:
            test_list = case.copy()
            func(test_list)
            print(f"{func.__name__}: {test_list}")