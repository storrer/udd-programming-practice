# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

def llstring(node: Optional[ListNode]):
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
""" Comments are for input list [1,2,4] """
class Solution:
    def reverseList_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case, approached as we move head up the links
        if head == None or head.next == None: # [1/2]= false, [2/4] =false, [3/None] = true
            return head # [3/None]
        # Recursive Case
        result_head = self.reverseList_recursive(head.next) # If head.next.next = None -> rev(head.next) returns itself and we set it as the new first link
        head.next.next = head # reverse the list direction here
        head.next = None
        return result_head
    """
    rev(1)
    """

    
    # Cleaner version mirrors LeetCode submission
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list_of_links = []
        if head == None or head.next == None:
            return head
        result_tail = ListNode(val=head.val) 
        
        assert isinstance(head.next,ListNode)

        while head != None:
            list_of_links.append(ListNode(val=head.val)) 
            head = head.next 
        for i in range(1,len(list_of_links)):
            list_of_links[i].next = result_tail
            result_tail = list_of_links[i]
        return result_tail

        
        
node1_3 = ListNode(4)
node1_2 = ListNode(2, node1_3)
node1_1 = ListNode(1, node1_2)

sol = Solution()
print(llstring(sol.reverseList_recursive(None))) # None
print(llstring(sol.reverseList_recursive(node1_3))) # Return this node
print(llstring(sol.reverseList_recursive(node1_1))) # [4,2,1]

