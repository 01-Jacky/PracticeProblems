class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


def make_linked_list(arr):
    head = ListNode(None)
    cur = head

    for i, el in enumerate(arr):
        cur.val = el
        if i != len(arr) - 1:
            cur.next = ListNode(None)
        cur = cur.next

    return head


def linked_list_to_list(head):
    elements = []

    while head:
        elements.append(head.val)
        head = head.next

    return elements
