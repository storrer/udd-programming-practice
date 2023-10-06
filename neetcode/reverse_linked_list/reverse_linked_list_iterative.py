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

class Solution:
    def reverseList_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list_of_links = []
        if head == None or head.next == None:
            return head
        result_tail = ListNode(head.val) # 1/None
        
        #list_of_links.append(result_tail) # [1/None]
        #assert isinstance(head.next,ListNode)

        while head != None:
            #new_head = ListNode(head.val, result_tail) #[2/1,1/None]
            list_of_links.append(ListNode(head.val)) # [1/None,2/None,
            #result_tail = new_head
            head = head.next # 1/2 -> 2/3 -> 3/None
        for i in range(1,len(list_of_links)): # 
            list_of_links[i].next = result_tail
            result_tail = list_of_links[i]
        return result_tail
    
    # Cleaner version mirrors LeetCode submission
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list_of_links = []
        if head == None or head.next == None:
            return head
        result_tail = ListNode(head.val)
        
        assert isinstance(head.next,ListNode)

        while head != None:
            list_of_links.append(ListNode(head.val)) 
            head = head.next 
        for i in range(1,len(list_of_links)):
            list_of_links[i].next = result_tail
            result_tail = list_of_links[i]
        return result_tail

        
        
node1_3 = ListNode(4)
node1_2 = ListNode(2, node1_3)
node1_1 = ListNode(1, node1_2)

sol = Solution()
print(llstring(sol.reverseList_iterative(None))) # None
print(llstring(sol.reverseList_iterative(node1_3))) # Return this node
print(llstring(sol.reverseList_iterative(node1_1))) # [4,2,1]

