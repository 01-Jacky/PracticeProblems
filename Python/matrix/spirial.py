import matrix_helper

# Strategy 1) Easy to understand but slow.
# Peel off top row. Rotate. Repeat until no elements left.
# Complexity: (n^2)
# Space: O(mn)

def rotate_counter(A):
    A[:] = zip(*A)      # Transpose
    A[:] = A[::-1]      # Reverse

def get_spiral_order(matrix):
    order = []
    while matrix:
        for el in matrix[0]:        # Get first row
            order.append(el)

        matrix[:] = matrix[1:]      # Strip the row and rotate counter clockwise
        rotate_counter(matrix)
    return order

matrix = [[1,2,3],[4,5,6],[7,8,9]]
s = ' '.join([str(el) for el in get_spiral_order(matrix)])
print(s)


# Strategy 2) more code but fast
# Use 4 integers to keep track of row/column start and end.
# Complexity: (n)
# Space: O(1)