class Solution(object):
    def roman_to_int(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        roman_int = 0
        previousValue = 0

        reversed = s[::-1]        
        for c in reversed:
            value = values[c]
            if value < previousValue:
                roman_int -= value
            else:
                roman_int += value
            previousValue = value

        return roman_int


inputs = [("III", 3), ("LVIII", 58), ("MCMXCIV", 1994)]
solution = Solution()
for input in inputs:
    if solution.roman_to_int(input[0]) == input[1]:
        print("Pass")
    else:
        print("Fail")