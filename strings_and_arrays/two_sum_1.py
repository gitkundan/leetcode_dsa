# two sum using pincer
# Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise.

# For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.

def two_sum_brute_force(a: list[int], target: int) -> bool:
    """Brute-force solution to find if any pair sums to target

    Args:
        a: Sorted list of unique integers
        target: Target sum to look for

    Returns:
        True if pair exists, False otherwise

    Complexity:
        Time: O(n²) - Nested loops checking all pairs
        Space: O(1) - No additional storage needed

    Drawbacks:
        - Very inefficient for large lists
        - Doesn't leverage the sorted input property
        - Duplicate work checking pairs in both orders
    """
    # Check all possible pairs using nested loops
    for first in a:
        # Compare with all subsequent elements
        for second in a[1:]:
            if first + second == target:
                return True  # Found a matching pair
    return False  # No pairs found

def two_sum_pairwise(a:list[int],target:int):
    i=0
    while i<len(a):
        if a[i]+a[i+1]==target:
            return True
        i+=1
    return False

def two_sum_two_pointers(nums: list[int], target: int) -> bool:
    """Two-pointer solution for finding target sum pair in sorted array

    Args:
        nums: Sorted list of unique integers (ascending order)
        target: Target sum value to find

    Returns:
        True if pair exists, False otherwise

    Complexity:
        Time: O(n) - Single pass through the list
        Space: O(1) - Only two pointers used

    Why the Logic is Reliable:
        Since the list is sorted in ascending order, moving the left pointer right always picks a larger number,
        increasing the sum, while moving the right pointer left picks a smaller number, decreasing the sum.
        If the current sum exceeds the target, any pair involving the current right value would be even larger
        with a bigger left, so safely discard that right value. Similarly, if the sum is less than the target,
        discard the current left value because smaller rights would make it even smaller. This elimination
        ensures no valid pair is missed, as proven in standard two-sum analyses for sorted inputs.
    """
    left = 0  # Start pointer at beginning of list
    right = len(nums) - 1  # End pointer at last element

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return True  # Found exact match

        # Adjust pointers based on comparison with target
        if current_sum > target:
            # Sum too big - move right pointer left to reduce sum
            right -= 1
        else:
            # Sum too small - move left pointer right to increase sum
            left += 1

    return False  # No pairs found after full traversal




#Usage:
a=[1,2,3]
# a=[9]
# a=[5,6,7]

# result=two_sum_brute_force(a,3)
result=two_sum_pairwise(a,5)
result=two_sum_two_pointers(a,5)

print(result)