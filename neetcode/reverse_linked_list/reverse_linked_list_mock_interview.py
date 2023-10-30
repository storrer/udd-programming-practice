# [1,2,3,4] -> [4,3,2,1]
# Constraints
# node.length >= 1
from typing import Optional



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def LinkedListToString(head):
    current = head
    
    while current:
        print(current.val)
        current = current.next
    
        

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Traverse through the list
        current = head
        previous = None

        while current:
            temp = current.next
            # Reverse the list, by reassigning .next
            current.next = previous
            previous = current
            current = temp

        # Head of reversed list
        return previous


# [1,2,3,4] -> [4,3,2,1] {val=4, next=ListNode(val=3 ...)}
link1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
link2 = ListNode(2)
sol = Solution()
LinkedListToString(sol.reverseList(link1))
LinkedListToString(sol.reverseList(link2))
#print(sol.reverseList(link1)
