# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = node = head
        while node.next:
            if node.val <= node.next.val:
                node = node.next
            else:
                pre = dummy
                while pre.next.val < node.next.val:
                    pre = pre.next
                tmp = node.next
                node.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
        return dummy.next
