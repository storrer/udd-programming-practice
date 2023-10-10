"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
1.
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
"""

# Definition for a binary tree node.
from typing import Optional

# root.val = 1
# root.left = null
# root.right = 2

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
 
            
        return 1 + max([self.maxDepth(root.left),self.maxDepth(root.right)])

# Inputs
root1 = TreeNode(val=1,right=TreeNode(val=2))
root2 = TreeNode(val=1,left=TreeNode(val=9),right=TreeNode(val=20, left=TreeNode(15),right=TreeNode(7)))
#[3,9,20,null,null,15,7]
sol = Solution()
print(sol.maxDepth(root1))
print(sol.maxDepth(root2))

