

    # Example 2: You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1". What is the length of the longest substring achievable that contains only "1"?

    # For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes 1111100111.

def find_length(s: str) -> int:
    """
    Finds the length of the longest substring containing at most one '0' after flipping.

    Args:
        s: Binary string consisting of '0's and '1's

    Returns:
        Length of the longest valid substring

    Time Complexity: O(n) - Single pass through the string
    Space Complexity: O(1) - Uses constant extra space
    """
    # curr is the current number of zeros in the window
    left = curr = ans = 0  # Initialize window pointers and counters
    for right in range(len(s)):
        # Expand window by including current character
        if s[right] == "0":
            curr += 1  # Count zeros in current window

        # Shrink window from left if more than one zero
        while curr > 1:
            if s[left] == "0":
                curr -= 1  # Decrement zero count when leaving window
            left += 1  # Move left pointer to shrink window

        # Update maximum window size found so far
        ans = max(ans, right - left + 1)

    return ans

#####=======###############

    # Example 3: 713. Subarray Product Less Than K. (https://leetcode.com/problems/subarray-product-less-than-k/)

    # Given an array of positive integers nums and an integer k, return the number of subarrays where the product of all the elements in the subarray is strictly less than k.

    # For example, given the input nums = [10, 5, 2, 6], k = 100, the answer is 8. The subarrays with products less than k are:

    # [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]


def subarray_product(nums: list[int], k: int) -> int:
    """
    Counts the number of subarrays with product less than k.

    Args:
        nums: List of positive integers
        k: Threshold product value

    Returns:
        Count of subarrays meeting the product condition

    Time Complexity: O(n) - Single pass through the array
    Space Complexity: O(1) - Uses constant extra space
    """
    if k <=1:
        return 0
    # Window tracking variables:
    left = ans = 0  # left=window start, ans=count of valid subarrays
    curr = 1        # curr=product of current window elements
    # Expand window by moving right pointer
    for right in range(len(nums)):  # right=window end
        # Expand window by multiplying current element
        curr *= nums[right]

        # Shrink window from left if product exceeds k
        while curr >= k:
            curr = curr // nums[left]  # Divide out leftmost element
            left += 1  # Move left pointer to shrink window

        # Count all subarrays ending at current right pointer
        ans += right - left + 1
    return ans

# Example 4: Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.
# this is not dynamic window but fixed window, build an initial window and then expand its size
def fixed_window_length(nums, k):
    # Return 0 if k is invalid
    if k <= 0 or k > len(nums):
        return 0
    curr = 0

    # build initial window
    for i in range(k):
        curr += nums[i]
    ans = curr


    # slide the window across rest of array
    for i in range(k, len(nums)):
        # Update the window sum by adding the new element and removing the last
        curr += nums[i] - nums[i - k]
        ans = max(ans, curr)

    return ans

# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.



# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000

#start here : https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4594/
# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
# remember the sliding window is moving pointer; to get the actual value still need to do nums[pointer]; do not sum every sliding window
def findMaxAverage(nums: list[int], k: int) -> float:
    # Calculate the sum of the first window
    curr_sum = 0
    for i in range(k):
        curr_sum += nums[i]

    max_sum = curr_sum

    # Slide the window across the rest of the array
    for j in range(k, len(nums)):
        # Update the sum by adding the new element and removing the first element of the previous window
        curr_sum += nums[j] - nums[j - k]

        # Update the maximum sum if the current window's sum is greater
        if curr_sum > max_sum:
            max_sum = curr_sum

    # Return the maximum average found
    return max_sum / k


# this is the official solution
def findMaxAverage_2(self, nums: list[int], k: int) -> float:
        curr = 0
        for i in range(k):
            curr += nums[i]

        ans = curr

        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            ans = max(ans, curr)

        return ans / k




# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]

def array_flip(nums:list[int],k:int):
    left=0
    max_size=0
    zero_counter=0

    for right in range(len(nums)):
        if nums[right]==0:
            zero_counter+=1
        while zero_counter>k:
            if nums[left]==0:
                zero_counter-=1
            left+=1
            max_size=max(max_size,right-left+1)
    return max_size





# nums = [1,1,1,0,0,0,1,1,1,1,0]
nums=[1,0,0,0]
k = 2
array_flip(nums,k)