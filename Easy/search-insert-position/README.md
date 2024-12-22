# Search Insert Position

## Problem Statement

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

## Example(s)

**Example 1:**

Input: `nums = [1, 3, 5, 6]`, `target = 5`  
Output: `2`  

**Example 2:**

Input: `nums = [1, 3, 5, 6]`, `target = 2`  
Output: `1`  

**Example 3:**

Input: `nums = [1, 3, 5, 6]`, `target = 7`  
Output: `4`  

## Solution Explanation

### Approach:
We can use a simple linear search to find the index where the target number should be inserted. We iterate over the array and compare each number with the target. If we find a number greater than or equal to the target, we return the current index. If we reach the end of the array, the target should be inserted at the end.

### Time Complexity:
- **O(n)**, where `n` is the length of the input array `nums`, since in the worst case, we need to iterate over the entire array.

### Space Complexity:
- **O(1)**, as we only use a few extra variables for the iteration and comp
