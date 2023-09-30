"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.+
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""


class Solution:
	def romanToInt(self, s: str) -> int:

		roman_to_int = {
			"I": 1,
			"V": 5,
			"X": 10,
			"L": 50,
			"C": 100,
			"D": 500,
			"M": 1000,
			#"IV": 4,
			#"IX": 10,
			#"XL": 40,
			#"XC": 90,
			#"CD": 400,
			#"CM": 900
		}
		roman_exceptions = {
			"IV": 4,
			"IX": 9,
			"XL": 40,
			"XC": 90,
			"CD": 400,
			"CM": 900
		}

		integer_value = 0
		"""		
		# Base solution
		for char in s:
			integer_value += roman_to_int[char]
		"""
		right = 1
		left = 0
		# "MCMXCIV"
		while left < len(s): #  n
			#print(right)
			if right < len(s): # constant
				current_string = "".join((s[left], s[right])) # constant
			else:
				current_string = s[left]

			# Check if s[left]+s[right] is an exception
			if current_string in roman_exceptions: # constant
				#print(f"Roman Exception found {current_string}")
				# If so increase integer_value accordingly and update left and right by 2
				integer_value += roman_exceptions[current_string]
				#print(f"Current value = {integer_value}")
				left += 2
				right += 2
			# If no exception, increase integer_value by roman_to_int[s[left]]
			else:
				integer_value += roman_to_int[s[left]]
				right += 1
				left += 1


		return integer_value
	

test_numbers = ["III", "LVIII", "MCMXCIV", "IV"]
#test_numbers = ["MCMXCIV"]

sol = Solution()
for test in test_numbers:
	print(sol.romanToInt(test))