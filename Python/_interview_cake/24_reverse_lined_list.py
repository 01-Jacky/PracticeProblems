class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

"""
1) Store previously visited nodes in a stack and rebuild a reversed list
Time: O(n)    Space:O(n)

2) Use a prev pointer and modify the next
Time: O(n)    Space:O(1)
"""

def reverse_nodes(node):
    prev = None
    cur = node

    while cur:
        scout = cur.next
        cur.next = prev
        prev = cur

        cur = scout
    return prev


d = LinkedListNode(4,None)
c = LinkedListNode(3,d)
b = LinkedListNode(2,c)
a = LinkedListNode(1,b)

a = reverse_nodes(a)
while a is not None:
    print(a.value)
    a = a.next

