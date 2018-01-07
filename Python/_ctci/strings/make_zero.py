import matrix_helper

def make_zero(matrix):
    zero_rows = set()
    zero_columns = set()

    # record
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_columns.add(j)

    # make rows zero
    for i in zero_rows:
        for j in range(len(matrix[0])):
            matrix[i][j] = 0

    # make column zero
    for j in zero_columns:
        for i in range(len(matrix)):
            matrix[i][j] = 0

matrix = [
        [1,2,3,4],
        [5,0,0,8],
        [1,2,3,4]
        ]
matrix_helper.print_matrix(matrix)
print()
make_zero(matrix)
matrix_helper.print_matrix(matrix)