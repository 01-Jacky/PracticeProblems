import matrix_helper


def _flipped(m):
    for i in range(len(m) // 2):
        # swap
        print(i)
        tmp = m[i]
        m[i] = m[len(m) - i - 1]
        m[len(m) - i - 1] = tmp
    return m


def _transpose(m):
    ans = []
    for col in range(len(m[0])):
        tmp = []
        for row in range(len(m)):
            tmp.append(m[row][col])
        ans.append(tmp)
    return ans

# def rotate(m):
#     # flip + transpose = clockwise rotation
#     # flipped = _flipped(m)
#     flipped = m[::-1]
#     return list(zip(*flipped))


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
