#https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head != None:
            start = head
            temp = head

            while temp.next != None:
                temp1 = temp.next
                start.next = temp1.next
                temp1.next = head
                head = temp1
                temp = start

        return head