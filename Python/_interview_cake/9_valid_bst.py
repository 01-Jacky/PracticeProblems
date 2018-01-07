"""
Validate a BST

1)
Max of left sub tree must be < than root value
Min of right sub tree must be > than root value

"""

def is_bst(root, min=float('-inf'), max=float('inf')):
    if root is None:
        return True

    return min < root.value < max and \
            is_bst(root.left, min, root.value) and \
            is_bst(root.right, root.value, max)


def is_binary_search_tree(root):
    node_and_bounds_stack = [(root, -float('inf'), float('inf'))]

    # depth-first traversal
    while len(node_and_bounds_stack):
        node, lower_bound, upper_bound = node_and_bounds_stack.pop()

        if (node.value <= lower_bound) or (node.value >= upper_bound):
            return False
        if node.left:   # this node must be less than the current node
            node_and_bounds_stack.append((node.left, lower_bound, node.value))
        if node.right:  # this node must be greater than the current node
            node_and_bounds_stack.append((node.right, node.value, upper_bound))

    # if none of the nodes were invalid, return true (at this point we have checked all nodes)
    return True