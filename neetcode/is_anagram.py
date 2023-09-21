"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
"""
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

s = "rat" 
t = "car"