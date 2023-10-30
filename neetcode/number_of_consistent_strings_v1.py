from typing import List


class Solution:
    # Go, C++ Style
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # Cast string into a set (faster containment lookups) , maybe later if allowed is larger for some reason
        
        count = 0 # mutable
        for word in words:
            if all(char in allowed for char in word): # generator
                count += 1
        
        return count
    
    # Ruby, Rust, Lisp
    def countConsistentFunctional(self, allowed, words):
        # no Mutables
        check = lambda word: all(char in allowed for char in word)
        consistent = filter(check, words)

        return len(list(consistent))


allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]

"""

nb: Functional programming avoids mutables.
Learn functional style! #TODO
"""