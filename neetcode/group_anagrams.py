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

is_anagram_counter = 0

word_shapes = {}

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

    """
    if s_count == t_count:
        return True
    else:
        return False    
    """
    global is_anagram_counter
    is_anagram_counter += 1

    return word_shapes[s] == word_shapes[t]


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagram_groups = []
    # If there are strings in the input array
    while strs:
        # Remove the first string from the input array
        # Create an output anagram group
        new_group = [strs.pop()] # O(n)
        # Take the first string, characterize it.
        # Move through the rest of the array
        unmatched_strings = []
        while strs:
            word = strs.pop()
            if isAnagram(new_group[0], word): # n = number of strings, m = length | n*m 
                # Remove matches, adding them to result group
                new_group.append(word)
            else:
                unmatched_strings.append(word)
        strs = unmatched_strings
        anagram_groups.append(new_group)

    return anagram_groups

test1 = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(test1))
#test2 = ["nozzle","punjabi","waterlogged","imprison","crux","numismatists","sultans","rambles","deprecating","aware","outfield","marlborough","guardrooms","roast","wattage","shortcuts","confidential","reprint","foxtrot","dispossession", "aaa", "aaba","lsadkj", "fjasl", "asdfj", "askjfe","sijo", "gasi", "jfio", "sjfo", "joij", "ashfie","jfowa", "wyuth", "fjolse", "ojhfs", "ahfowss", "fhoiehj", "fjoseehu", "fhjksbbb", "jfowskahjkss"]
#print(groupAnagrams(test2))
#test3 = ["a"]
#print(groupAnagrams(test3))
#TODO get this down to O(n*m)
#TODO work on this with mark D tomorrow
print(is_anagram_counter)

#TODO keep consistent code between here and leetcode