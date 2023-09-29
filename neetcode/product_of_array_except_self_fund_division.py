"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

What if instead of using the division operation we just used a 
fundamental division algorithm. For example if The product of all elements 
in the array was 15 and the current element contains the number 3, we 
obtain the product of all other elements besides the current element by 
essentially dividing the product of all elements in the array by the 
quotient of 15 and 3. However, we find the quotient by using a fundamental 
division algorithm rather than the division operator. For dividing 15x3 we 
would start with the divisor, 3, and begin adding it to itself while 
counting how many times the number 3 must be used in an addition expression 
until the dividend is reached. In this example we must add five 3s to get 
15, therefore our quotient is five, and the product of all other elements 
except this element is five. An array in which this operation could occur 
is [3,1,1,5].
"""

from typing import List

class Solution:
    def quotient(self, dividend: int, divisor: int) -> int:
        
        # The quotient is found by counting iterations of loop below
        quotient = 0
        # Sum is used to control how many times we must add divisor
        sum = 0
        while sum < dividend:   # Until sum reaches dividend
            sum += divisor      # Add divisor to sum
            quotient += 1       # and increment quotient

        return quotient

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)

        return []
    
test_nums1 = [2,3,4]
i = test_nums1[0]
sol = Solution()
sol.productExceptSelf(test_nums1)