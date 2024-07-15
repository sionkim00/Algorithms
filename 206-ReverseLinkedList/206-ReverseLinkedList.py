        prev = None

        while head:
            nxt = head.next
            head.next = prev
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
[
