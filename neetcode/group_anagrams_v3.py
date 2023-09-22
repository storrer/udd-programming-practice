"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""


#is_anagram_counter = 0

#word_shapes = {}
"""
def isAnagram(s, t):
	#print(f"s: {s} and t: {t}")
	if s not in word_shapes:		
		s_count = {}
		for letter in s:
			if letter in s_count:
				s_count[letter] += 1
			else:
				s_count[letter] = 1
		word_shapes[s] = s_count
	
	if t not in word_shapes:
		t_count = {}
		for letter in t:
			if letter in t_count:
				t_count[letter] += 1
			else:
				t_count[letter] = 1
		word_shapes[t] = t_count

	#global is_anagram_counter
	#is_anagram_counter += 1

	return word_shapes[s] == word_shapes[t]
"""

import cProfile
from typing import List

class Solution:
	@classmethod
	def groupAnagrams(cls, strs: List[str]) -> List[List[str]]:

		# Create a dictionary to store the sorted word shapes.
		sorted_word_shapes = {}
		for word in strs:
			sorted_word_shape = str(sorted(word))
			if sorted_word_shape not in sorted_word_shapes:
				sorted_word_shapes[sorted_word_shape] = []
			sorted_word_shapes[sorted_word_shape].append(word)

		# Return the values of the dictionary as a list.
		anagram_groups = []
		for sorted_word_shape, strs in sorted_word_shapes.items():
			anagram_groups.append(strs)

		return anagram_groups

if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    anagram_groups = Solution.groupAnagrams(strs)

    # Profile the code.
    cProfile.run('Solution.groupAnagrams(strs)')

test1 = ["eat","tea","tan","ate","nat","bat"]
print(Solution.groupAnagrams(test1))
test2 = ["nozzle","punjabi","waterlogged","imprison","crux","numismatists","sultans","rambles","deprecating","aware","outfield","marlborough","guardrooms","roast","wattage","shortcuts","confidential","reprint","foxtrot","dispossession", "aaa", "aaba","lsadkj", "fjasl", "asdfj", "askjfe","sijo", "gasi", "jfio", "sjfo", "joij", "ashfie","jfowa", "wyuth", "fjolse", "ojhfs", "ahfowss", "fhoiehj", "fjoseehu", "fhjksbbb", "jfowskahjkss"]
print(Solution.groupAnagrams(test2))
#test3 = ["a"]
#print(Solution.groupAnagrams(test3))
#print(is_anagram_counter)
