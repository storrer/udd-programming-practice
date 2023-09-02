"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""


def is_palindrome(s: str) -> bool:
    # preprocess string here (don't be afraid to 'refactor')
    return s.upper().replace(" ", "").replace(".","")[::-1] == s.upper().replace(" ","").replace(".","")

s_test = "abba"
s_test_two = "abb a"
s_test_three = "abb. a"

print(is_palindrome(s_test))
print(is_palindrome(s_test_two))
print(is_palindrome(s_test_three))

# Run more often!
# Test new code and edge cases.
# Try 'teacher mode' - asides and details about the code, language at hand.
# Use type suggestions in function def
# "Premature optimization is the root of all evil"
# Don't brood -- speak.
# Practice like this next week.
import os
os.g