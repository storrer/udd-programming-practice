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
    def find_left_peak(self, arr):
        left = 0
        right = 1
        peak = 0
        rightmost_peak = len(arr) - 2

        while right <= rightmost_peak:
            if arr[left] < arr[right]:
                peak = right
            else:
                return peak
            left += 1
            right += 1
        return peak
        # examine arr[left] and arr[left + 1]
        
    def find_right_peak(self, arr):
        right = len(arr) - 1
        left = right - 1
        
        return 0

    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        isValidMountain = True
        
        # Find left peak
        left_peak = self.find_left_peak(arr)
        # find right peak
        right_peak = self.find_right_peak(arr)
        # If right peak and left peak are the same index, return true

        # If not the same index then we have a possible plateau or none-valid array

        


        return isValidMountain
    
arr1 = [0,3,2,1,0]
arr2 = [0,1,2,3,0]

sol = Solution()
print(sol.find_left_peak(arr1))
print(sol.find_left_peak(arr2))


