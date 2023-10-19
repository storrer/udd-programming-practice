"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

[]

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:

1. The number of nodes in the tree is in the range [1, 10^4].
2. -2^31 <= Node.val <= 2^31 - 1
"""




# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def validate_recursive_left(self, root, maximum, minimum):
        if root is None:
            return True
        
        if root.val >= maximum:  
            return False
        
        if root.val < minimum:
            minimum = root.val
        return self.validate_recursive_left(root.left, maximum, minimum) and self.validate_recursive_right(root.right, maximum, minimum)
    

    def validate_recursive_right(self, root, maximum, minimum):
        if root is None:
            return True
        
        if root.val <= minimum:
            return False
        
        if root.val > maximum:
            maximum = root.val
        return self.validate_recursive_left(root.left, maximum, minimum) and self.validate_recursive_right(root.right, maximum, minimum)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True     
       
        left_is_valid_bst = self.validate_recursive_left(root.left, root.val, root.val)
        right_is_valid_bst = self.validate_recursive_right(root.right, root.val, root.val)

        return left_is_valid_bst and right_is_valid_bst
    



sol = Solution()
#[3,9,20,null,null,15,7]
root2 = TreeNode(val=3,left=TreeNode(val=2),right=TreeNode(val=20, left=TreeNode(15),right=TreeNode(21)))
root3 = TreeNode(val=4,left=TreeNode(val=2,left=TreeNode(val=1),right=TreeNode(val=3)),right=TreeNode(val=6,left=TreeNode(val=5),right=TreeNode(val=7)))
root4 = TreeNode(val=4,left=TreeNode(val=-299,left=TreeNode(val=1),right=TreeNode(val=3)),right=TreeNode(val=6,left=TreeNode(val=5),right=TreeNode(val=7)))


print(sol.isValidBST(root2))
print(sol.isValidBST(root3))
print(sol.isValidBST(root4))



