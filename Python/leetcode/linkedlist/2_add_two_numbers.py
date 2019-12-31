"""https://leetcode.com/problems/add-two-numbers/submissions/"""
# Definition for singly-linked list.

from Python.helper.linkedlist import make_linked_list, linked_list_to_list

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = 0
        factor = 1

        while l1 or l2:
            loop_sum = 0
            if l1:
                loop_sum += l1.val
            if l2:
                loop_sum += l2.val

            # Carry
            if loop_sum >= 10:
                sum += 10*factor

            sum += loop_sum % 10 * factor

            # iterate
            l1, l2 = _next_node(l1, l2)
            factor *= 10

        return _int_to_linked_list(sum)

def  _next_node(l1, l2):
    l1 = l1.next if l1 is not None else None
    l2 = l2.next if l2 is not None else None
    return l1, l2


def _int_to_linked_list(num):
    head = ListNode(None)
    cur = head
    s = str(num)[::-1]

    for i, digit in enumerate(s):
        cur.val = int(digit)
        if i != len(s) - 1:
            cur.next = ListNode(None)
        cur = cur.next
    return head


l1 = make_linked_list([1,2])
l2 = make_linked_list([0])

ans = Solution().addTwoNumbers(l1, l2)
print(linked_list_to_list(ans))