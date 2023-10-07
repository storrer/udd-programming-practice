"""
Height-Balanced
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
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

