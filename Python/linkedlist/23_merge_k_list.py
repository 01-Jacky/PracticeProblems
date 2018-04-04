"""
1) Do merge 2 list k-1 times
Time O(nk) Space O(n)

2) Merge k list using a pq that keeps track of all the heads at once
Time O(n log k) Space O(n)

Put all the heads in a PQ
remove from PQ and add to final list
"""


class Solution(object):
    def mergeKLists(self, lists):
        from queue import PriorityQueue
        head = ListNode(0)
        cur = head
        q = PriorityQueue()

        for node in lists:                  # Init PQ
            if node:
                q.put((node.val, node))     # Want PQ ordered by node values so we can't just put node into PQ

        while not q.empty():
            value, node = q.get()

            cur.next = ListNode(value)      # Put it in the answer
            cur = cur.next

            node = node.next                # If that specific list has more nodes to process
            if node:
                q.put((node.val, node))

        return head.next