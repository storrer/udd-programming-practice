"""
Write a function that takes a string prefix as an argument and returns an array of all of 
the words that contain that prefix.
"""

class Solution:
    # O(kn) = O(n) | k = len(prefix)
    def words_with_prefix(self, prefix):
        result = []

        with open('sowpods.txt', 'r') as file:
            word: str
            for word in file:
                word = word.rstrip()
                if word.startswith(prefix):
                    result.append(word)
            

        return result

sol = Solution()
print(sol.words_with_prefix("CAT"))

# TIME COMPLEXITY DISCUSSION
# Attribute 'weeding': length of string must be => prefix
# Attribute: is n sorted? If so we can 'weed' out 
# repetition not a constraint: create a cache of 'seen' words
# It's fair game to assume that a library function is optimized
# however some languages have functions that are known to be not optimized
# Java builders > string appends


# # O(kn) = O(n) | k = len(prefix) is different from O(nm) in that n and m are variable inputs
