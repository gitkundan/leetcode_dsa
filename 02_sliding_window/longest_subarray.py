# Let's say that we are given a positive integer array nums and an integer k. We need to find the length of the longest subarray that has a sum less than or equal to k. For this example, let nums = [3, 2, 1, 3, 1, 1] and k = 5.


def longest_subarray_bruteforce(nums: list[int], k: int) -> int:
    """
    Finds the length of the longest subarray with a sum <= k using a brute-force approach.

    Args:
        nums: List of positive integers
        k: Target maximum sum for the subarray

    Returns:
        Length of the longest subarray meeting the sum condition

    Time Complexity: O(n²) - Checks all possible subarrays
    Space Complexity: O(1) - Uses constant extra space
    """
    max_length = 0
    n = len(nums)
    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += nums[end]
            if current_sum <= k:
                max_length = max(max_length, end - start + 1)
            else:
                # If sum exceeds k, no need to check longer subarrays from this start
                break
    return max_length

# Example usage:
nums = [3, 2, 1, 3, 1, 1]
k = 5
print(f"Brute-Force Result: {longest_subarray_bruteforce(nums, k)}")

def longest_subarray_sliding_window(nums: list[int], k: int) -> int:
    """
    REMEMBER : THIS IS NOT PINCER BUT CATERPILLAR MOVEMENT
    Finds the length of the longest contiguous subarray with sum <= k using sliding window.

    This function implements a caterpillar-style sliding window algorithm:
    - Expands by moving the right pointer
    - Shrinks by moving the left pointer when sum exceeds k

    Args:
        nums: List of positive integers
        k: Target maximum sum for the subarray

    Returns:
        Length of the longest subarray meeting the sum condition

    Time Complexity: O(n) - Single pass through the array
    Space Complexity: O(1) - Uses constant extra space
    """
    left = 0
    curr_sum = 0
    max_length = 0

    for right in range(len(nums)):
        # Add the next element to the window
        curr_sum += nums[right]

        # Shrink the window from the left if the sum is too large
        while curr_sum > k:
            curr_sum -= nums[left]
            left += 1

        # Update the maximum length found so far
        # The left and right pointers define the window boundaries:
        # - left: window start (inclusive)
        # - right: window end (inclusive)
        # - window is nums[left..right] inclusive
        max_length = max(max_length, right - left + 1)

    return max_length

# --- Example Usage ---

# Example 1: Find the longest subarray with sum <= 8
nums1 = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k1 = 8
result1 = longest_subarray_sliding_window(nums1, k1)
print(f"For nums = {nums1} and k = {k1}:")
print(f"The length of the longest subarray is: {result1}")
# Expected output: 4 (corresponding to the subarray [4, 2, 1, 1])

print("-" * 20)

# Example 2: A case where the entire array is a valid window
nums2 = [1, 2, 3, 4]
k2 = 10
result2 = longest_subarray_sliding_window(nums2, k2)
print(f"For nums = {nums2} and k = {k2}:")
print(f"The length of the longest subarray is: {result2}")
# Expected output: 4 (corresponding to the subarray [1, 2, 3, 4])



# Example usage:
nums = [3, 2, 1, 3, 1, 1]
k = 5
print(f"Sliding Window Result: {longest_subarray_sliding_window(nums, k)}")