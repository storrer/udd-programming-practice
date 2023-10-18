"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order_list = []
        current_level = []
        child_level = []
        if root is None:
            return [] 
        if root.left is None and root.right is None:
            level_order_list.append(current_level.append(root.val))
            return level_order_list # [[root.val]]
        
        # [[3],[4,5], [6,7]]

        

        def traverse_two_levels(root, curr, child):
            curr.append(root.val)
            if root.left is not None:
                child.append(root.left.val) 
                #child_level.append(root.left) then replace nodes with values in a loop?
            if root.right is not None:
                child.append(root.right.val)

            return (curr, child)
        
        current_level.append(root.val)
        current_level = []
        child_level.append(root.left)
        child_level.append(root.right)
        
        
        new_child = []
        for node in child_level:
            current_level.append(node.val)
            new_child.append(node.left)
            new_child.append(node.right)
        level_order_list.append(current_level)
        child_level = new_child

        # append current level to result and clear it
        # replace current_level objects with keys at the same time

        
        children_remaining = True
        # if root.left and right are None, flip to False and end a loop
        




        #if there is a third level on root.left.left than do the steps above
        # create another two result lists 

        #def traverse(root):
            # Going from left to right, append node values to current_level list, finally append to level_order_list

            # Then 'move' down one level and read values from left to right for next level

        return level_order_list
        


        

    
sol = Solution()

root2 = TreeNode(val=3,left=TreeNode(val=2),right=TreeNode(val=20, left=TreeNode(15),right=TreeNode(21))) # [3, 2, None, None, 20, 15, 21]

root3 = TreeNode(val=3, left=TreeNode(val=4),right=TreeNode(val=5)) # [[3],[4,5]]
root3 = TreeNode(val=3, left=TreeNode(val=4, left=TreeNode(val=6)),right=TreeNode(val=5, right=TreeNode(val=7))) # [[3],[4,5], [6,7]]


print(sol.levelOrder(root3))