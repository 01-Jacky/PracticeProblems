class LinkedNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    """ Queries """
    def peek(self):
        if self.size == 0:
            raise ValueError("queue is empty")
        return self.head.value

    def size(self):
        return self.size

    """ Actions """
    def enqueue(self, item):
        if self.size == 0:
            self.head = LinkedNode(item)
            self.tail = self.head
        else:
            self.tail.next = LinkedNode(item)
            self.tail = self.tail.next
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise ValueError("queue is empty")
        removed = self.head
        self.head = self.head.next
        self.size -= 1
        return removed.value

    def find(self, value):
        pass

    def delete(self, value):
        pass


q = Queue()
q.enqueue(1)
print(q.dequeue())
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
