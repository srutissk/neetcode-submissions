# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        removeIndex = len(nodes) - n
        if removeIndex == 0:
            return head.next
        
        nodes[removeIndex - 1].next = nodes[removeIndex].next
        return head