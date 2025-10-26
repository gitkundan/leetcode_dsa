"""
Determines if one string is a subsequence of another using two-pointer technique.

A subsequence of a string is a sequence of characters that can be obtained by deleting
some (or none) of the characters from the original string, while maintaining the
relative order of the remaining characters.

Examples:
- "ace" is a subsequence of "abcde"
- "aec" is NOT a subsequence of "abcde"
"""

def is_subsequence(sub: str, main: str) -> bool:
    """
    Check if 'sub' is a subsequence of 'main' string.
    
    Args:
        sub: Potential subsequence string to search for
        main: Main string to search within
    
    Returns:
        True if all characters in 'sub' appear in 'main' in order, False otherwise
    
    Time Complexity: O(n) where n is length of main string
    Space Complexity: O(1) - uses only pointers
    """
    sub_ptr = main_ptr = 0  # Initialize pointers for both strings
    
    # Traverse both strings simultaneously
    while sub_ptr < len(sub) and main_ptr < len(main):
        if sub[sub_ptr] == main[main_ptr]:
            # Match found, move to next character in subsequence
            sub_ptr += 1
        # Always move main string pointer forward
        main_ptr += 1
    
    # If we exhausted all characters in subsequence, it's a match
    return sub_ptr == len(sub)
