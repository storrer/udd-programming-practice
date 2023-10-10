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
    depths = {}
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        if root in self.depths:
            return self.depths[root]

        self.depths[root] = 1 + max([self.maxDepth(root.left),self.maxDepth(root.right)])
        return self.depths[root]

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        if abs(self.maxDepth(root.left) -  self.maxDepth(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        return False

# Inputs
root1 = TreeNode(val=1,right=TreeNode(val=2))
#[3,9,20,null,null,15,7]
root2 = TreeNode(val=3,left=TreeNode(val=9),right=TreeNode(val=20, left=TreeNode(15),right=TreeNode(7)))
# Example 2
root3 = TreeNode(val=1, left= TreeNode(val=2,left=TreeNode(val=3,left=TreeNode(val=4), right=TreeNode(val=4)),right=TreeNode(val=3)),right=TreeNode(val=2))
sol = Solution()
print(sol.isBalanced(root1))
print(sol.isBalanced(root2))
print(sol.isBalanced(root3))


#MEMOIZE