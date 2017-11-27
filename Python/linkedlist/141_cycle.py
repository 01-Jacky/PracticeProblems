# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False

        c1 = head
        c2 = head
        while c2.next is not None and c2.next.next is not None:
            c1 = c1.next
            c2 = c2.next.next
            if c1 == c2:
                return True
        return False

