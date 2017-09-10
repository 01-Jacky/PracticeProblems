"""
https://leetcode.com/problems/intersection-of-two-linked-lists/description/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def _get_lst_len(self, head):
        len_lst = 0
        while head:
            len_lst += 1
            head = head.next
        return len_lst


    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        len_A = self._get_lst_len(headA)
        len_B = self._get_lst_len(headB)

        # Get the two list to start at the same length
        diff_len = abs(len_A - len_B)
        if len_A > len_B:
            for x in range(diff_len):
                headA = headA.next
        else:
            for x in range(diff_len):
                headB = headB.next

        # Move them at the same pace and check for intersection
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None


if __name__ == "__main__":
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    b1 = ListNode(1)

    a1.next = a2
    a2.next = a3
    b1.next = a2

    print Solution().getIntersectionNode(a1, b1)


