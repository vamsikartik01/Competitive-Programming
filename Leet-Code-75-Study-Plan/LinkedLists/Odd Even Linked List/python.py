# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head != None and head.next != None:
            odd = head
            even = head.next

            while even.next != None:
                temp = even.next
                even.next = temp.next
                temp.next = odd.next
                odd.next = temp
                odd = odd.next
                temp = even
                if even.next != None:
                    even = even.next
            
        return head