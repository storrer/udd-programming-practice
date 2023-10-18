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

-105 <= Node.val <= 105

pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next
 
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # If head, the first link, is None our linked list does not cycle
        # If the first link points to None, our list does not cycle
        if head is None or head.next is None:
            return False
        
        # Store the seen objects in a quick lookup collection
        seen = set()

        def traverse(link) -> bool:
            if link in seen:
                return True
            else:
                seen.add(link)
            if link.next is None:
                return False
            return traverse(link.next)
        
        assert isinstance(head.next,ListNode)

        temp = head
        while temp.next is not None:
            # Check current link for having been seen
            if temp in seen:
                return True
            else:
                seen.add(temp)
            if temp.next is None:
                return False
            temp = temp.next
        
        return False
    

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

