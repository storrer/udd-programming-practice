"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        # Default value is 0
        self.val = val
        self.next = next # Starts with none, the end of the list
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        print(*list1)
        return

node1_3 = ListNode(4)
node1_2 = ListNode(2, node1_3)
node1_1 = ListNode(1, node1_2)

node2_3 = ListNode(4)
node2_2 = ListNode(3, node2_3)
node2_1 = ListNode(1, node2_2)


def return_list_string(node: Optional[ListNode]):
    if node is None:
        return "[]"
    node_exists = node # Resolve this is 'unwrapped'
    # Incremental Step
    result = "["
    result += str(node.val) # add first node
    while node_exists.next is not None:
        node_exists = node_exists.next
        result += ','
        result += str(node_exists.val)
    result += "]"
    return result


print(return_list_string(None))
print(return_list_string(node1_1))
print(return_list_string(node2_1))

sol = Solution()
#sol.mergeTwoLists()
"""
1
[1,2,4] 
[1,3,4]
2
[2,4] head1
[3,4] head2
[1,1] tail = node2_1
3
if head2 < head1:
    swap them
else
    tail.next = head1
[1,1,2]
    tail = tail.next
    tail.next = head2
[1,1,2,3]
    

"""