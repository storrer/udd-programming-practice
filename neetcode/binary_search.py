"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.

"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Determine size of array is binary searchable
        low = 0
        high = len(nums) - 1

        while low < high:
            # Calculate guess index
            guess = (low + high) // 2
            guess_value = nums[guess]
            if guess_value == target:
                return guess
            elif guess_value < target:
                low = guess + 1
            elif guess_value > target:
                high = guess - 1

        if nums[low] == target:
            return low
        # No match found
        return -1
    


test1 = [-1,0,3,5,9,12]
target1 = 9 # expected is 4
sol = Solution()
print(sol.search(test1,target1))