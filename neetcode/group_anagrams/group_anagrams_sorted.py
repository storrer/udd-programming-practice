from typing import List

import cProfile

class Solution:
	@classmethod
	def groupAnagrams(cls, strs: List[str]) -> List[List[str]]:
		# Create a dictionary to store the sorted word shapes.
		sorted_word_shapes = {}
		for word in strs:
			print(word, sorted(word))
			# String representation of the sorted word, can be replaced with string method "".join()
			sorted_word_shape = str(sorted(word))
			if sorted_word_shape not in sorted_word_shapes:
				sorted_word_shapes[sorted_word_shape] = []
			sorted_word_shapes[sorted_word_shape].append(word)

		# Return the values of the dictionary as a list.
		anagram_groups = []
		for sorted_word_shape, strs in sorted_word_shapes.items():
			anagram_groups.append(strs)

		return anagram_groups
	
test1 = ["eat","tea","tan","ate","nat","bat"]
print(Solution.groupAnagrams(test1))

if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    anagram_groups = Solution.groupAnagrams(strs)

    # Profile the code.
    cProfile.run('Solution.groupAnagrams(strs)')
