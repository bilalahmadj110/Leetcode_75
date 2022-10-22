# https://leetcode.com/problems/merge-two-sorted-lists


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# Note: You don't always need to get a single node of a linked list to append to another.
        
class Solution(object):
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(next=None)
        cur_output = dummy
        
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    cur_output.next = list1
                    list1 = list1.next
                else:
                    cur_output.next = list2
                    list2 = list2.next
            elif list1:
                cur_output.next = list1
                list1 = list1.next
            else:
                cur_output.next = list2
                list2 = list2.next     
            cur_output = cur_output.next
                    
        return dummy.next
        
        
        
if __name__ == "__main__":
    pass