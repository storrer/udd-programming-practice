# Brute force solution
"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Input: nums = [1,2,3,1]
Output: true
"""
"""
Original implementation.
def contains_duplicate(numbers):
    nums_set = set(numbers) # (1,2,3) | (1,2,3,4) |(-1)
    for num in nums_set: # O(n)
        numbers.remove(num) # O(n) 
    if not numbers: # Unique by default
        return False
    # This is where we need improvement 
    for num in nums_set: # O(n)
        if num in numbers: # O(n)
            return True
        
    return False
"""
def contains_duplicate(numbers):
    # use a set to keep track of seen numbers
    seen_nums = set()
    for num in numbers:
        if num in seen_nums:
            return True
        else:
            seen_nums.add(num)

nums_one = [1,2,3,1] # should be True
nums_two = [1,2,3,4] # False
nums_three = [1,1,1,3,3,4,3,2,4,2]
nums_four = [-1]
nums_five = [-1,2,1,-2,-100,100] # False