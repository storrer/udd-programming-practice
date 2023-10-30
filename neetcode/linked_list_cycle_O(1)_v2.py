"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 10^4].

-10^5 <= Node.val <= 10^5

pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

inp = [1,2] # Expected False

class Solution:
    def hasCycle(self, head: Optional[ListNode]):        
        normal = head
        fast = head

        while fast.next is None:
            # something with the pointers
            fast = normal.next.next
            if normal is fast:
                return True



node1_3 = ListNode(4)
node1_2 = ListNode(2, node1_3)
node1_1 = ListNode(1, node1_2)

sol = Solution()
print(sol.hasCycle(None)) # False
print(sol.hasCycle(node1_3)) # False
print(sol.hasCycle(node1_1)) # False

node2_3 = ListNode(4)
node2_2 = ListNode(2, node2_3)
node2_1 = ListNode(1, node2_2)
node2_3.next = node2_1

print(sol.hasCycle(node2_1)) # True

