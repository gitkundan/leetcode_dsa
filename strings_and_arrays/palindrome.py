# Palindrome checker using two-pointer technique
def check_if_palindrome(s: str):
    """Determine if a string reads the same forward and backward.

    Args:
        s: Input string to check

    Returns:
        True if palindrome, False otherwise

    Complexity:
        Time: O(n) - Single pass through half the string
        Space: O(1) - Uses only two pointers
    """
    # Initialize pointers: left at start, right at end of string
    left = 0
    right = len(s) - 1

    # Continue while pointers haven't met or crossed
    # We use < instead of <= because:
    # - For odd lengths, middle character doesn't need comparison
    # - For even lengths, pointers will cross when done
    while left < right:
        # If characters don't match, it's not a palindrome
        if s[left] != s[right]:
            return False
        # Move pointers towards center
        left += 1
        right -= 1

    # All character pairs matched - it's a palindrome
    return True


def check_if_palindrome_brute_force(s: str):
    """Simplistic palindrome check using string reversal

    Args:
        s: Input string to check

    Returns:
        True if palindrome, False otherwise

    Note:
        This approach creates a reversed string for comparison.

    Complexity:
        Time: O(n) - Reversing string takes linear time
        Space: O(n) - Stores reversed string in memory
    """
    return s == s[::-1]


# values to test
value = "racecar"  # this is palindrome
# value='none' # this is not a palindrome
check_if_palindrome(value)
