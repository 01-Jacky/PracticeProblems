# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Solution 1) recursion
    # Time: O(n) Space: O(1)
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self._reverse(head, None)

    def _reverse(self, cur, prev):
        if cur is None:
            return prev
        next_node = cur.next
        cur.next = prev
        return self._reverse(next_node, cur)


    # Solution 2) use 3 pointers and iterate through the list
    # Time: O(n) Space: O(1)
    # def reverseList(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     if head is None:
    #         return None
    #
    #     prev = None
    #     cur = head
    #
    #     while head is not None:
    #         next = cur.next
    #         cur.next = prev
    #         cur = next
    #     return prev

