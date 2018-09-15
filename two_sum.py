## Problem
# Given an array of integers, return indices of the two numbers 
    # such that they add up to a specific target.
# You may assume that each input would have exactly one solution, 
    # and you may not use the same element twice.

## Complexity Analysis:
# Time complexity : O(n)O(n). 
    # We traverse the list containing nn elements only once. 
    # Each look up in the table costs only O(1)O(1) time.
# Space complexity : O(n)O(n). 
    # The extra space required depends on the number of items stored 
    # in the hash table, which stores at most nn elements.

def two_sum(nums, target):
    map = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in map:
            return [map[complement], i]
        map[nums[i]] = i
