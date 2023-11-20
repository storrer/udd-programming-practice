# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        
        # Check that values are the same for the two nodes
        if p.val != q.val:
            return False
        
        # Recur with the left children of both p and q, and recur with the right children
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None or subRoot is None:
            return False
        
        return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

p = TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3)) 
q = TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))
r = TreeNode(val=1, left=TreeNode(val=3, left=q), right=TreeNode(val=2))

sol = Solution()
print(sol.isSubtree(r,q)) # True