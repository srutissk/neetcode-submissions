# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # brute force
        """
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
        """
        # two pointers (4)
        temp = ListNode(0, head)
        left = temp
        right = head

        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return temp.next