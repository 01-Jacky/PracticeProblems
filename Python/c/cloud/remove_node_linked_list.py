""" remove node in linked list """


def remove_node(head, k):
    # Make this a header linked list to simplify cases where we might need to delete the front
    header = ListNode('header node')
    header.next = head
    prev = header
    cur = head

    while cur is not None:
        if cur.val == val:
            prev.next = cur.next
        else:
            prev = prev.next

        cur = cur.next

    return header.next

"""
delete a
delete b
delete c

h -> a -> c -|
    p     c

"""