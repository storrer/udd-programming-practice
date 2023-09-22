import cProfile
from typing import List



class Solution:
	@classmethod
	def groupAnagrams(cls, strs: List[str]) -> List[List[str]]:
		#sorted_word_shapes = {}
		sorted_word_shapes : dict[tuple,List[str]] = {}
		# For each word create a list of 26 zeros
		
		for word in strs:
			letter_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			for letter in word:
				letter_counts[ord(letter) - 97] += 1
			letter_counts = tuple(letter_counts)
			if letter_counts not in sorted_word_shapes:
				sorted_word_shapes[letter_counts] = []
			sorted_word_shapes[letter_counts].append(word)

		# Return the values of the dictionary as a list.
		#anagram_groups = []
		#print(sorted_word_shapes)
		return list(sorted_word_shapes.values())
	
test1 = ["eat","tea","tan","ate","nat","bat"]
print(Solution.groupAnagrams(test1))

if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    anagram_groups = Solution.groupAnagrams(strs)

    # Profile the code.
    cProfile.run('Solution.groupAnagrams(strs)')
