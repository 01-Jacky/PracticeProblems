import matrix_helper


def rotate(A):
    A[:] = A[::-1]
    A[:] = zip(*A)


def print_matrix(matrix):
    for row in matrix:
        for el in row:
            print(el, end=' ')
        print()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
matrix_helper.print_matrix(matrix)
print()
rotate(matrix)
matrix_helper.print_matrix(matrix)

