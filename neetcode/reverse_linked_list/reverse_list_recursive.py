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
    def reverse_list_rec(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None: # [1/2]= false, [2/4] =false, [3/None] = true
            return head # [3/None]
        # Recursive Case
        result_head = self.reverse_list_rec(head.next) # If head.next.next = None -> rev(head.next) returns itself and we set it as the new first link
        head.next.next = head # reverse the list direction here
        head.next = None
        return result_head


node1_3 = ListNode(4)
node1_2 = ListNode(2, node1_3)
node1_1 = ListNode(1, node1_2)

sol = Solution()
print(llstring(sol.reverse_list_rec(None))) # None
print(llstring(sol.reverse_list_rec(node1_3))) # Return this node
print(llstring(sol.reverse_list_rec(node1_1))) # [1,2,4] [4,2,1]

# Construct circular list
# 