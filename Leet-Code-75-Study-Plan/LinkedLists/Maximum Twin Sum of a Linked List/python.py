# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fptr = head
        sptr = head
        while fptr.next.next != None:
            fptr = fptr.next.next
            sptr = sptr.next
        miniHead = sptr

        if miniHead != None:
            start = miniHead
            temp = miniHead

            while temp.next != None:
                temp1 = temp.next
                start.next = temp1.next
                temp1.next = miniHead
                miniHead = temp1
                temp = start

        maxSum = 0

        ptr = head
        while ptr != None:
            sm = ptr.val+miniHead.val
            maxSum = max(maxSum, sm)
            ptr = ptr.next
            miniHead = miniHead.next

        return maxSum

        