from typing import Optional
class TreeNode:
    def __init__(self, val=0.0, left=None, right=None):
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

# TDD TBD
p = TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))
q = TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))
r = TreeNode(val=1, left=TreeNode(val=3), right=TreeNode(val=2))
s = None
t = TreeNode(val=1.5)
# TODO Coverage!
u = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=3)))
v = TreeNode(val=1, right=TreeNode(val=2, right=TreeNode(val=3)))

sol = Solution()
print(sol.isSameTree(p,q))
print(sol.isSameTree(p,r))
print(sol.isSameTree(p,s))
print(sol.isSameTree(p,t))
print(sol.isSameTree(p,u))
print(sol.isSameTree(p,v))
print(dir(TreeNode))


