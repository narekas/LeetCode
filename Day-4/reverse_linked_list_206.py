# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return head
        if not head.next: return head
        orig_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return orig_head 
