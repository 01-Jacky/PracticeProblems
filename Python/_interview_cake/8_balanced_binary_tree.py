"""
A tree is "superbalanced" if the difference between the depths of any two leaf nodes is no greater than one.

Solution:
1) Traverse all tree nodes and record their depth


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


def is_balanced(tree_root):
    if tree_root is None:
        return True

    depths = []  # we short-circuit as soon as we find more than 2

    # we'll treat this list as a stack that will store tuples of (node, depth)
    nodes = []
    nodes.append((tree_root, 0))

    while len(nodes):
        node, depth = nodes.pop()

        if (not node.left) and (not node.right):
            # case: leaf
            if depth not in depths:
                depths.append(depth)

                # two ways we might now have an unbalanced tree:
                #   1) more than 2 different leaf depths
                #   2) 2 leaf depths that are more than 1 apart
                if (len(depths) > 2) or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
                    return False
        else:
            # case: this isn't a leaf - keep stepping down
            if node.left:
                nodes.append((node.left, depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))
    return True

def is_balanced_v2(root):
    stack = []
    depths = set()
    stack.append((root,0))

    while stack:
        popped, depth = stack.pop()

        if not popped.left and not popped.right:    # If leaf node
            depths.add(depth)
        else:
            if popped.left:
                stack.append((popped.left, depth+1))
            if popped.right:
                stack.append((popped.right, depth+1))

    if max(depths) - min(depths) > 1:
        return False
    else:
        return True

# Okay
a = BinaryTreeNode('a')
b = BinaryTreeNode('b')
c = BinaryTreeNode('c')
d = BinaryTreeNode('d')
e = BinaryTreeNode('e')
f = BinaryTreeNode('f')
g = BinaryTreeNode('g')

a.left = b
a.right = c

b.left = d
c.left = e
c.right = f

f.right = g

print(is_balanced(a))
print(is_balanced_v2(a))

# Okay
a = BinaryTreeNode('a')
b = BinaryTreeNode('b')
c = BinaryTreeNode('c')
d = BinaryTreeNode('d')
e = BinaryTreeNode('e')
f = BinaryTreeNode('f')
g = BinaryTreeNode('g')

a.left = b
a.right = c

b.left = d
c.right = f

f.right = g
g.left = e

print(is_balanced(a))
print(is_balanced_v2(a))