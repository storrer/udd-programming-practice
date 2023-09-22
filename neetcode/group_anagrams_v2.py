from typing import List


class Solution:
	word_shapes = {}
	is_anagram_counter = 0
	# O(n)
	def isAnagram(self, s, t):
		#print(f"s: {s} and t: {t}")
		if s not in self.word_shapes:		
			s_count = {}
			for letter in s:
				if letter in s_count:
					s_count[letter] += 1
				else:
					s_count[letter] = 1
			self.word_shapes[s] = s_count
		
		if t not in self.word_shapes:
			t_count = {}
			for letter in t:
				if letter in t_count:
					t_count[letter] += 1
				else:
					t_count[letter] = 1
			self.word_shapes[t] = t_count

		"""
		if s_count == t_count:
			return True
		else:
			return False	
		"""
		#global is_anagram_counter
		#is_anagram_counter += 1
		# Comparing two dictionaries
		return self.word_shapes[s] == self.word_shapes[t]


	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		anagram_groups = []
		# local variable length_hash
		length_hash = {}

		# Create length_hash
		for word in strs:
			if len(word) in length_hash:
				length_hash[len(word)].append(word)
			else:
				length_hash[len(word)] = [word]

		print(f"Length Hash: {length_hash.items()}")
		# If there are strings in the input array
		# These whiles are O(m)^2
		while strs:
			# Remove the first string from the input array
			# Create an output anagram group
			new_group = [strs.pop()]
			# Take the first string, characterize it
			# Move through the rest of the array
			#unmatched_strings = []
			base_word = new_group[0]
			print(base_word)
			#while strs:
			i = 0
			
			for word in length_hash[len(base_word)]: 
				
				if word != base_word and self.isAnagram(base_word, word): # n = number of strings, m = length | n*m 
					# Remove matches, adding them to result group
					new_group.append(word)
					strs.remove(word)
					#length_hash[len(base_word)].remove(word)
					#length_hash[len(base_word)].remove(base_word)

				#else:
					#unmatched_strings.append(word)
			#strs = unmatched_strings
			print("New Group collected!", new_group)
			anagram_groups.append(new_group)

		return anagram_groups
	
# 
# Complexity of is_anagram?
# " " " groupAnagrams
length_hash = {5: ["apple", "pears", "fruit"]}
# 1) for each item in the length_hash key
# 2) call isanagram
word_shapes = {}

# 3) if isAnagram ->
new_group = []
new_group.append("apple")
length_hash[5].remove("apple")

ga = Solution()

test1 = ["eat","tea","tan","ate","nat","bat"]
print("test one", ga.groupAnagrams(test1))
test2 = ["nozzle","punjabi","waterlogged","imprison","crux","numismatists","sultans","rambles","deprecating","aware","outfield","marlborough","guardrooms","roast","wattage","shortcuts","confidential","reprint","foxtrot","dispossession", "aaa", "aaba","lsadkj", "fjasl", "asdfj", "askjfe","sijo", "gasi", "jfio", "sjfo", "joij", "ashfie","jfowa", "wyuth", "fjolse", "ojhfs", "ahfowss", "fhoiehj", "fjoseehu", "fhjksbbb", "jfowskahjkss"]
#print("test two", ga.groupAnagrams(test2))

#TODO test on leetcode
#TODO find other attributes (length) by which to iterate or sort or group the words