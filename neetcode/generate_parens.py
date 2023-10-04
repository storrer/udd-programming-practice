"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 
Input: n = 2
Output: ["(())"] # (( 2 opens in a row
Constraints:

1 <= n <= 8
"""

from typing import List
class Solution:
    def generate_suffixes(self, prefix, n)-> List[str]:
        result = []
        if len(prefix) == 2*n:
            return [prefix] # Base case, magic case
        if prefix.count('(') < n:
            result += self.generate_suffixes(prefix + '(', n) # Increment
        if prefix.count('(') > prefix.count(')'):
            result += self.generate_suffixes(prefix + ')', n) # Increment
        return result        



    def generateParenthesis(self, n: int) -> List[str]:
        result_list = self.generate_suffixes("" , n)
        




        return result_list

sol = Solution()
print(sol. generateParenthesis(4))