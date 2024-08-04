# Data Structures
These are Exercises from Grokking Data Structures & Algorithms for Coding Interviews
## Arrays
### Problem 1
Given a one-dimensional array of integers, create a new array that represents the running sum of the original array.

The running sum at position i in the new array is calculated as the sum of all the numbers in the original array from the 0th index up to the i-th index (inclusive). Formally, the resulting array should be computed as follows: result[i] = sum(nums[0] + nums[1] + ... + nums[i]) for each i from 0 to the length of the array minus one.

Input: [2, 3, 5, 1, 6]
Expected Output: [2, 5, 10, 11, 17]

