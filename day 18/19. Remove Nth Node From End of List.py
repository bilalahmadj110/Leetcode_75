# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        prev = None
        cur = head
        remove = head
        while cur:
            
            if n <= 0:
                prev = remove
                remove = remove.next
            n -= 1
            cur = cur.next
        if remove == head:
            return head.next
        if prev:
            prev.next = remove.next if remove else None
        else:
            return None
        return head