# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # brute force
        """
        if not head:
            return 
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        i, j = 0, len(nodes) - 1
        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            if i >= j:
                break
            nodes[j].next = nodes[i]
            j -= 1
        
        nodes[i].next = None
        """
        # recursion (2)
        def rec(root: ListNode, curr: ListNode) -> ListNode:
            if not curr:
                return root
            
            root = rec(root, curr.next)
            if not root:
                return None
            
            temp = None
            if root == curr or root.next == curr:
                curr.next = None
            else:
                temp = root.next
                root.next = curr
                curr.next = temp
            
            return temp

        head = rec(head, head.next)