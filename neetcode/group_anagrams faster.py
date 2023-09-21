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
from typing import List


#TODO rewrite isAnagram
def isAnagram(s, t):
	s_count = {}
	for letter in s:
		if letter in s_count:
			s_count[letter] += 1
		else:
			s_count[letter] = 1
	
	t_count = {}
	for letter in t:
		if letter in t_count:
			t_count[letter] += 1
		else:
			t_count[letter] = 1
	"""
	if s_count == t_count:
		return True
	else:
		return False
	"""
	return s_count == t_count

 
def groupAnagrams(strs: List[str]) -> List[List[str]]:
	anagram_groups = []
	# If there are strings in the input array
	while strs:
		# Remove the first string from the input array
		# Create an output anagram group
		new_group = [strs.pop(0)] 
		# Take the first string, characterize it
		# Move through the rest of the array
		i = 0
		while i < len(strs):
			if isAnagram(new_group[0], strs[i]):
				new_group.append(strs[i])
				strs.remove(strs[i])
			else:
				i += 1
		anagram_groups.append(new_group)

	return anagram_groups

test1 = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(test1))

#TODO get this down to O(n*m)
#TODO work on this with mark D tomorrow

