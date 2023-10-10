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
 
"""

from typing import List

#def product_of_prefix(index,prefix=[1]):
#    """Find product of all elements in subarray"""
#    if index - 1 == -1:
#        return 1
#    else:
#        prefix = nums[index]*prefix[]
#        return product_of_prefix(nums,index-1,prefix)
#    return product

#def suffix_product(nums, index):
#    """Find product of all elements in subarray nums[index+1:]"""
#    product = 1 # for last index, for loop will not run
#    for i in range(index+1, len(nums)): # right of current index
#        product *= nums[i]
#    return product




class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Find the product of the elements in the list to the left
        # of each element
        prefix_array = [1]
        for i in range(1,len(nums)):
            current_prefix = prefix_array[i-1] * nums[i-1]
            prefix_array.append(current_prefix)
        print(prefix_array)
        suffix_array = [1]*len(nums)
        print(suffix_array)
        for i in range(len(nums)-2,-1,-1):
            print(i)
            current_suffix = suffix_array[i+1] * nums[i+1]
            suffix_array[i] = current_suffix
        print(suffix_array)
        result_array = []
        for i in range(len(nums)):
            result_array.append(prefix_array[i] * suffix_array[i])
        return result_array
    
test_nums1 = [2,3,4]
sol = Solution()
print(f"Final result: {sol.productExceptSelf(test_nums1)}")
