from TreeNode import TreeNode
from sys import path
path.append('E:\\Projects\\udd-programming-practice\\scripts_and_tools\\')
from clockdeco import clock

@clock
def find_min_max(root:TreeNode):
    minimum = root.val
    return min(minimum, find_min(root.left,minimum), find_min(root.right,minimum))
    
def find_min(root:TreeNode|None, minimum):
    if root is None:
        return minimum
    if root.left is None and root.right is not None:
        return min(find_min(root.right,minimum))
    if root.right is None and root.left is not None:
        return min(find_min(root.left,minimum))
    if minimum is None:
        minimum = root.val
    if root.val < minimum:
        minimum = root.val
    
    return min(find_min(root.left,minimum),find_min(root.right,minimum))

root2 = TreeNode(val=3,left=TreeNode(val=9),right=TreeNode(val=20, left=TreeNode(15),right=TreeNode(7)))
root3 = TreeNode(val=4,left=TreeNode(val=2,left=TreeNode(val=1),right=TreeNode(val=3)),right=TreeNode(val=6,left=TreeNode(val=5),right=TreeNode(val=7)))

root4 = TreeNode(val=4,left=TreeNode(val=-299,left=TreeNode(val=1),right=TreeNode(val=3)),right=TreeNode(val=6,left=TreeNode(val=5),right=TreeNode(val=7)))

print(find_min_max(root2))
print(find_min_max(root3))
print(find_min_max(root4))
