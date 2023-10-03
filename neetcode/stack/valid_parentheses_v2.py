"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists 
of parentheses only '()[]{}'.
"""



from clockdeco import clock


s1 = "()" # Valid
s2 = "(]" # hanging closed, unclosed open
s3 = "(())" # Nested
s4 = "(())("

class Solution:
    
    @classmethod
    @clock
    def isValid(cls, s: str) -> bool:
        matched_parens = ["()", "{}", "[]"]
        invalid_pairs = ["(}", "(]", "{]", "{)", "[}", "[)"]
        # 1. Open and then closing must be detected,
        stack = []
        for char in s:
            # if stack is empty, append current char to stack (push)
            if len(stack) ==  0:
                stack.append(char)
            # elif stack[-1] is complement of current char than pop [-1] and continue | match found
            elif stack[-1] + char in matched_parens:
                stack.pop() 
            # at this point it is not a complement
            elif stack[-1] + char in invalid_pairs:
                return False
            else: # Must be a opening paren
                stack.append(char)


        # if anything left on stack i.e. unclosed or unopened parens
        if len(stack) > 0:
            return False
        return True # stack empty and no more char
    
def run_tests():
    test_inputs = [("()[]{}", True), ("(])", False), ("sf[a1]", False), ("{{(([[[((((({{{{{}}}}})))))]]]))}}", True), ("(){", False)]
    test_passed = True
    for test in test_inputs:
        if Solution.isValid(test[0]) != test[1]:
            test_passed = False
            print(f"Failed on input {test[0]}\nExpected: {test[1]}")
    if test_passed:
        print("Pass")

if __name__ == "__main__":
    run_tests()
