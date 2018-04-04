# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
1) Store each step and check at the end like a regular string
Time O(n) Space O(n)
1) Get to the end
Time O(n) Space O(n)
"""


class Solution(object):
    def reverseList(self, head):
        prev = None
        cur = head

        while cur is not None:
            scout = cur.next
            cur.next = prev
            prev = cur
            cur = scout

        return prev

    def isPalindrome(self, head):
        # Find the midpoint
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse from the midpoint
        head_right = self.reverseList(slow)

        # Check in palindrome


