"""
Integer list, any duplicates return true.
"""
from typing import List
from clockdeco import clock
class Solution:
	@clock
	def containsDuplicate(self, nums: List[int]) -> bool:
		
		if not nums:
			return False
		# store a set of seen items
		seen_numbers = set()

		for number in nums:
			if number in seen_numbers:
				return True
			seen_numbers.add(number)

		return False

if __name__ == "__main__":
	def runTests():
		sol = Solution()
		test_empty_list = ([], False)
		test_true1 = ([1,2,3,3], True)
		test_false1 = ([1,2,3,4,10], False) 
	
		test_passed = True
		test_inputs = [test_empty_list, test_true1, test_false1]
		for input in test_inputs:
			test_result = sol.containsDuplicate(input[0])
			if test_result != input[1]:
				print(f"Input: {input[0]} Expected: {input[1]} Actual: {test_result}")
				test_passed = False

		
		if test_passed:
			print("All test passed.")

	runTests()