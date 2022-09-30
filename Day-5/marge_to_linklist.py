# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l1, l2):
    w = m = ListNode(None)
    while l1 and l2 : 
        if l1.value <= l2.value :
            w.next, l1 = l1, l1.next
        else : 
            w.next, l2 = l2, l2.next
        w = w.next
    if not l1 : w.next = l2
    if not l2 : w.next = l1
    return m.next
