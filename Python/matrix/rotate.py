import matrix_helper


def rotate(A):
    """
    Reverse and transpose (counter clockwise)
    Time: O(mn) Space: O(mn)
    """
    A[:] = A[::-1]
    A[:] = zip(*A)


matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
matrix_helper.print_matrix(matrix)
print()
rotate(matrix)
matrix_helper.print_matrix(matrix)
