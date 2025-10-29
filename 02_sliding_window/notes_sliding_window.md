The sliding window is an algorithmic technique for efficiently solving problems that involve contiguous subarrays or substrings. It works by maintaining a "window" over a portion of the data, which slides from the beginning to the end of the sequence . This approach avoids the inefficiency of re-evaluating overlapping parts of the data, typically reducing the time complexity from a brute-force O(n²) to a linear O(n) .

### Core Concepts

The technique uses two pointers, often named `left` and `right`, to define the boundaries of the current window. The window is initially small and expands by moving the `right` pointer. When the window no longer satisfies a specific condition (making it "invalid"), it shrinks by moving the `left` pointer forward .

A common pattern in these problems is the concept of a "valid" subarray, which is defined by two parts :
*   **Constraint Metric**: An attribute of the subarray, such as its sum, product, or the count of specific elements.
*   **Numeric Restriction**: A condition applied to the metric, such as being less than or equal to a value `k`.

### How It Works

The algorithm iterates through the array while adjusting the window's size:
1.  **Expand**: The `right` pointer moves one step at a time, adding a new element to the window.
2.  **Check Validity**: After adding an element, the algorithm checks if the window still meets the problem's constraints.
3.  **Shrink**: If the window is invalid (e.g., its sum exceeds a target), the `left` pointer moves forward, removing elements from the beginning of the window until it becomes valid again.
4.  **Update Answer**: In each valid state, the algorithm updates the result (e.g., the maximum length or count found so far) .

This process ensures that each element is visited by the `left` and `right` pointers at most once, leading to an efficient O(n) runtime .

### Common Problem Types

The sliding window pattern is versatile and can be adapted to solve several types of problems.

#### Dynamic Window Size
The window size changes by expanding and shrinking to find the optimal subarray that satisfies a condition.
*   **Example**: Find the length of the longest subarray whose sum is less than or equal to `k`.
*   **Logic**: The window expands to the right. If the sum exceeds `k`, the window shrinks from the left until the sum is valid again. The maximum length is tracked throughout the process .

#### Fixed Window Size
The window maintains a constant size `k` as it slides across the array.
*   **Example**: Find the subarray of a fixed length `k` with the largest sum.
*   **Logic**: An initial window of size `k` is formed. As the window slides one position to the right, one new element is added and one old element is removed, maintaining the fixed size. The answer is updated at each step .

#### Counting Subarrays
This variation counts the total number of valid subarrays.
*   **Example**: Find the number of subarrays where the product of elements is less than `k`.
*   **Logic**: For a valid window ending at index `right` with a starting index `left`, there are `right - left + 1` valid subarrays ending at that position. This quantity is added to the total count in each step .

### Implementation and Efficiency

A general implementation uses a `for` loop to iterate the `right` pointer and a nested `while` loop to advance the `left` pointer when the window is invalid. A variable is used to track the constraint metric (e.g., `currentSum`) in O(1) time, avoiding costly recalculations .

*   **Time Complexity**: **O(n)**. Although there is a nested loop, the `left` pointer only moves forward, so the total number of operations is proportional to the size of the array (amortized analysis) .
*   **Space Complexity**: **O(1)**, as it typically only requires a few variables to store the pointers and the current state of the window's metric .

## General approach
```bash
FUNCTION sliding_window(array, condition_parameter):
  // 1. Initialize pointers and state variables
  left = 0
  max_result = 0
  // Initialize other state variables as needed (e.g., window_sum, char_counts)

  // 2. Iterate through the array with the right pointer to expand the window
  FOR right FROM 0 TO length(array) - 1:
    // 2a. Update state based on the new element entering the window
    current_element = array[right]
    // (e.g., add current_element to window_sum, or increment its count in a hash map)

    // 3. Check if the window is now invalid. If so, shrink it from the left.
    WHILE window_is_invalid(condition_parameter):
      // 3a. Get the element that is about to leave the window
      leaving_element = array[left]

      // 3b. Update state by "removing" the leaving_element
      // (e.g., subtract leaving_element from window_sum, or decrement its count)

      // 3c. Physically shrink the window by moving the left pointer
      left = left + 1

    // 4. At this point, the window is guaranteed to be valid.
    // Calculate the current window's size and update the result.
    current_size = right - left + 1
    max_result = max(max_result, current_size)

  // 5. Return the final result after checking all possible windows
  RETURN max_result
END FUNCTION
```