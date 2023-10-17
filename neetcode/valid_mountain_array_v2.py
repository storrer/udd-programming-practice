"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] `5t< arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

Example 1:

Input: arr = [2,1]
Output: false

Example 2:

Input: arr = [3,5,5]
Output: false

Example 3:

Input: arr = [0,3,2,1]
Output: true
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
"""
from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        increasing = True

        for i in range(len(arr)):
            #TODO add index check to beginning of loop
            if (i + 1) >= len(arr):
                continue
            if increasing and arr[i] < arr[i + 1]: 
                continue # We're increasing legally, continue iterating through array
            elif not increasing and arr[i] < arr[i + 1]:
                return False # We've peaked but started increasing after a decrease or plateau
            elif increasing and arr[i] > arr[i + 1] and i > 0:
                increasing = False
            elif arr[i] == arr[i + 1]:
                return False # Plateau
            elif increasing:
                return False # Increasing to the end, invalid mountain
            
        return not increasing
    
arr1 = [0,3,2,1,0]
arr2 = [0,1,2,3,0]
arr3 = [0,3,2,3,0]
arr4 = [0,1,2,3,4,5,6,7,8,9]
arr5 = [9,8,7,6,5,4,3,2,1,0] # Expected False

sol = Solution()
print(sol.validMountainArray(arr1))
print(sol.validMountainArray(arr2))
print(sol.validMountainArray(arr3))
print(sol.validMountainArray(arr4))
print(sol.validMountainArray(arr5))





