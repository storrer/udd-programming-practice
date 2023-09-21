"""
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        # Indexes delimiting substring
        left = 0
        
        # Substring attribute
        max_length = 1

        # Loop over the string
        for right in range(1, len(s)):
            #TODO rewrite 42 with a hash lookup
            #TODO maintain the set or dict
            # If letter repeats, update right index
            if s[right] in s[left:right]:
                # Update starting index
                left = s.index(s[right], left) + 1
                continue
            
            current_length = right - left + 1

            if current_length > max_length:
                max_length = current_length

        return max_length
    
test1 = "abcabcbb" # 3
test2 = "bbbbb" # 1 
test3 = "pwwkew" # 3
test4 = "okayy" 

sol = Solution()

print(sol.lengthOfLongestSubstring(test1), "exp 3")
print(sol.lengthOfLongestSubstring(test2), "exp 1")
print(sol.lengthOfLongestSubstring(test3), "exp 3")
print(sol.lengthOfLongestSubstring(test4), "exp 4")

