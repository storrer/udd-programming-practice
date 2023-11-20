"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""

class Solution:
	def isPalindrome(self, s: str) -> bool:
		s = "".join(filter(str.isalnum, s.lower()))
		#print(s)

		return s == s[::-1]

sol = Solution()
print(sol.isPalindrome("abba.|")) # true
s1 = "A man, a plan, a canal: Panama"
print(sol.isPalindrome(s1)) # true


#sol = Solution()
s_test = "abba"

s_test_two = "abc a"
#s_test_three = "abb. a"

print(sol.isPalindrome(s_test)) # true
print(sol.isPalindrome(s_test_two)) # False
#print(sol.isPalindrome()(s_test_three))

# Run more often!
# Test new code and edge cases.
# Try 'teacher mode' - asides and details about the code, language at hand.
# Use type suggestions in function def
# "Premature optimization is the root of all evil"
# Don't brood -- speak.
# Practice like this next week.