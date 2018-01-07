class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

"""
1) Store previously visited nodes in a set and check each time
Time: O(n)    Space:O(n)

2) Use 2 pointers, fast and slow
The faster one will either finish or catch up to slow
Note faster will never pass slow 
    (faster node gains on slower one by distance of 1 each iteration... so distance shrinks by 1 and until it is 0)
    (proof by contradiction.... if faster passed)
Time: O(n)    Space:O(1)
"""

def has_cycle(node):
    c_slow = node
    c_fast = node

    while c_fast is not None and c_fast.next is not None:
        c_slow = c_slow.next
        c_fast = c_fast.next.next

        if c_slow == c_fast:
            return True

    return False    # reached the end


d = LinkedListNode(4,None)
c = LinkedListNode(3,d)
b = LinkedListNode(2,c)
a = LinkedListNode(1,b)
# d.next = b

print(has_cycle(a))