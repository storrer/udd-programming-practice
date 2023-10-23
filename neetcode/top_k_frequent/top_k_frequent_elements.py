"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
 

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""

from typing import List
from collections import Counter

class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a empty collection of counts
		counts = {}
		# Iterate through the input nums
		for number in nums: # O(n)
			# If number in collection
			if number in counts.keys():
				# Increment count by 1
				counts[number] += 1
			# If not we add the number to the collection and its count = 1
			else:
				counts[number] = 1

		print(f"Counts' keys and values {counts.items()}")	
		# Find the top k numbers and return them
		sorted_counts = sorted(counts.items(),key=lambda x: x[1], reverse=True) # O(nlog(n))
		print(f"Sorted counts: {sorted_counts}")

		# Collect the top K elements in sorted_counts
		top_k_numbers = [x[0] for x in sorted_counts[:k]] # O(n)

		return top_k_numbers
	
	def top_k_frequent(self, nums, k):
		counts = Counter(nums)

		sorted_counts = sorted(counts.items(),key=lambda x: x[1], reverse=True) # O(nlog(n))
		print(f"Sorted counts: {sorted_counts}")

		# Collect the top K elements in sorted_counts
		top_k_numbers = [x[0] for x in sorted_counts[:k]] # O(n)

		return top_k_numbers
	
test_nums1 = [1,1,1,2,2,3]
k1 = 2
# Expected Output: [1,2]
sol = Solution()
print(sol.topKFrequent(test_nums1, k1))
print(sol.top_k_frequent(test_nums1, k1))

