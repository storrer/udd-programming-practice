"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

Constraints:

- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order.
- -1000 <= target <= 1000
The tests are generated such that there is exactly one solution. 
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]|None:
        #1. brute force: iterate over the array for each element
        #2. set(numbers) - if target - current_element in set(numbers) ! no index given
        #3. Two pointer:
        left = 0
        right = len(numbers) - 1
        
        while numbers[left] + numbers[right] != target:
            sum = numbers[left] + numbers[right]   
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            if left == right:
                return None
        

        return [left+1, right+1]
    


# Tests
sol = Solution()

numbers1 = [2,7,11,15]
target1 = 9
print("Actual: ",sol.twoSum(numbers1,target1), " Expected [1,2]")

numbers11 = [1,2,3]
target11 = 12
print("Actual: ",sol.twoSum(numbers11,target11), " Expected None")

numbers12 = [1,2,3,4]
target12 = 12
print("Actual: ",sol.twoSum(numbers12,target12), " Expected None")




numbers2 = [2,3,4]
target2 = 6
print("Actual: ",sol.twoSum(numbers2,target2), " Expected [1,3]")

numbers3 = [-1,0]
target3 = -1
print("Actual: ",sol.twoSum(numbers3,target3), " Expected [1,2]")

 