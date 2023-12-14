# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next:
            fptr = head.next
            sptr = head
            while fptr.next != None and fptr.next.next != None:
                fptr = fptr.next.next
                sptr = sptr.next

            if sptr.next != None:
                if sptr.next.next != None:
                    sptr.next = sptr.next.next
                else:
                    sptr.next = None
        
        else:
            head = None
        
        return head