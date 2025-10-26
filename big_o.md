# Big O Notation

## Introduction to Algorithms

An algorithm is a step-by-step recipe for a computer to solve a problem. It takes an input and produces an output, which is the answer to a question regarding the input.

**Requirements for LeetCode Algorithms:**

*   **Deterministic:** Given the same input, the algorithm should always produce the same output.
*   **Correct:** The algorithm should be correct for any arbitrary valid input.

## Big O Notation

Big O notation describes the computational complexity of an algorithm, which is split into time complexity and space complexity.

*   **Time Complexity:** How much longer does the algorithm take to complete as the input size grows?
*   **Space Complexity:** How much more memory does the algorithm use as the input size grows?

Complexity is described by a function, where the variables represent values that change between different inputs and affect the algorithm (e.g., `n` for the length of an input array).

Examples of complexities:

*   O(n)
*   O(n^2)
*   O(log n)

## Calculating Complexity

The function calculates the number of operations or amount of memory your algorithm consumes relative to the input size.

**Rules:**

1.  **Ignore Constants:** O(9999999n) = O(n)
2.  **Consider Complexity as Variables Tend to Infinity:** O(2n + n^2 - 500n) = O(n^2)

The best complexity possible is O(1), called "constant time" or "constant space".

**Cases:**

*   Best case scenario
*   Average case
*   Worst case scenario (most correct to use)

## Analyzing Time Complexity

*   **O(n):** Iterating through an array once.
*   **O(n^2):** Nested loops iterating through an array.
*   **O(n+m):** Iterating through two arrays of different lengths.

## Logarithmic Time

O(log n) means that the input is being reduced by a percentage at every step (e.g., binary search).
O(logn) means that somewhere in your algorithm, the input is being reduced by a percentage at every step. A good example of this is binary search, which is a searching algorithm that runs in O(log⁡n)O(logn) time . With binary search, we initially consider the entire input (n elements). After the first step, we only consider n / 2 elements. After the second step, we only consider n / 4 elements, and so on. At each step, we are reducing our search space by 50%, which gives us a logarithmic time complexity.

## Analyzing Space Complexity

*   **O(1):** Constant space, regardless of input size.
*   **O(n):** Space grows linearly with input size (e.g., storing `n` integers in an array).
*   **O(n*m):** Space grows with the product of two input sizes (e.g., creating an `n x m` grid).