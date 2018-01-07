"""
1) Get to the largest 1st, then use find largest again


"""
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def find_largest(root_node):
    current = root_node
    while current:
        if not current.right:
            return current.value
        current = current.right

# Cake solution
def find_second_largest(root_node):
    if root_node is None or \
            (root_node.left is None and root_node.right is None):
        raise Exception('Tree must have at least 2 nodes')

    current = root_node
    while current:
        # case: current is largest and has a left subtree
        # 2nd largest is the largest in that subtree
        if current.left and not current.right:
            return find_largest(current.left)

        # case: current is parent of largest, and largest has no children,
        # so current is 2nd largest
        if current.right and \
           not current.right.left and \
           not current.right.right:
            return current.value

        current = current.right


# Mine
def find_largest_node_v2(root):
    if root is None:
        return -1

    cur = root
    while cur.right:
        cur = cur.right
    return cur.value

def find_second_largest_v2(root):
    # Need at least 2 node
    if root is None or (root.left is None and root.right is None):
        return -1

    cur = root
    while cur:
        # Reached largest and there's left subtree
        if cur.right is None and cur.left is not None:
            return find_largest_node_v2(cur.left)

        # right child is a leaf node then we're on the second largest node!
        if cur.right is not None and (cur.right.left is None and cur.right.right is None):
            return cur.value

        cur = cur.right


a = BinaryTreeNode('a')
b = BinaryTreeNode('b')
c = BinaryTreeNode('c')
d = BinaryTreeNode('d')
e = BinaryTreeNode('e')
f = BinaryTreeNode('f')
g = BinaryTreeNode('g')

a.left = b
a.right = c

c.left = e
c.right = f
f.left = g
g.right = d

print(find_second_largest_v2(a))