"""
Write a function that takes a string substring as an argument and returns an array of all of 
the words that contain that substring (the substring can appear anywhere in the word).
"""

class Solution:
    # O(n times m) | 
    def words_with_substring(self, substring):
        result = []

        with open('sowpods.txt', 'r') as file:
            word: str
            for word in file:
                word = word.rstrip()
                if word.count(substring):
                    result.append(word)
            

        return result

sol = Solution()
print(sol.words_with_substring("CAT"))

# TIME COMPLEXITY DISCUSSION
# Attribute 'weeding': length of string must be => substring
# repetition not a constraint: create a cache of 'seen' words
# 
