"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

We are going to solve this 3 different ways today.

1. Brute Force
2. Two Pointer Solution
3. Using a Dict
"""
nums = [15,11,2,7]
target = 9
# Output: [0,1]

# function that takes nums[] as input, and target
def brute_two_sum(nums: list, target):
	# compare each element + each following element to the target
	for i in range(len(nums)): # 2
		#TODO tidyup
		current_el = nums[i] # 2
		for j in range(i+1,len(nums)): # 3
			if current_el + nums[j] == target: # true
				# The first time we find a much, return the indices
				return [i,j] # [2,3]

# nums = nums
# target = 9
# i 0
nums = [15,11,2,7]
target = 9
# Output: [2,3]
sorted = [2,7,11,15]

# Two Pointer solution
def two_pointer_two_sum(nums: list, target):
	# sort the list in place with built in method
	# nums.sort() # O(nlog(n))
	# Preprocessing not considered in the complexity UNLESS it
	#TODO use a tuple to sort by element keeping indices 
	# nums.sort(key=lambda x:x)
	nums_list = list(enumerate(nums))
	nums_list.sort(key=lambda x:x[1])

	# Compare the first and last elements
	left = 0 # number 2
	right = len(nums) - 1 # 15

	while nums_list[left][1] + nums_list[right][1] != target:
		if nums_list[left][1] + nums_list[right][1] > target:
			right -= 1
		elif nums_list[left][1] + nums_list[right][1] < target:
			left += 1
	
	return [nums_list[left][0],nums_list[right][0]]

nums = [15,11,2,7]
target = 9

def set_two_sum(nums: list, target):
	# Use a set
	nums_set = set(nums)
	# {2, 11, 7, 15}
	for i in range(len(nums_set)):
		if target - nums[i] in nums_set: # O(1)
			return [nums[i], target - nums[i]]
		
def dict_two_sum(nums: list, target):
	nums_dict = {}
	for index, element in enumerate(nums):
		nums_dict[element] = index

	for i in range(len(nums)):
		# ensure that target - nums[i] is not nums_dict[target - nums[i]]
		if target - nums[i] in nums_dict and i != nums_dict[target - nums[i]]:
			return [i, nums_dict[target-nums[i]]]


#TODO Time vs Space tradeoffs